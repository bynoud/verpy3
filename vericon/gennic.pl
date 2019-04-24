#!/usr/bin/env perl

use lib "/user/ductt/bin/perllib";
use VeriConn;

use strict;
use warnings;

my $nicname = "nic400_fbrc_nic_cpu_jtag";
set_topname "fbrc_nic_wrap";

## ID bitwidth setup (pex_cfg/eth_cfg need ID gen)
my %idw = (
    nvus_cpu    => 8,
    nvus_pex    => 8,
    pexs        => 6,
    roms        => 12,
    msix        => 13,
    tcms        => 15,
);

my %clks = (
    pexs    => 'axi_aclk',
    pexm    => 'axi_aclk',
    # default will be 'clk_out1'
);

read_verilog "../$nicname/nic400/verilog/$nicname.v";
read_verilog "../fbrc_id_gen.v";
read_verilog "../fbrc_id_remap_axi4.v";
#read_verilog "../fbrc_nicv2_dbg.v";

compile;

# combined reset
# pop-generate for ID remap
new_assigns q/
    resetn = ~(~nicresetn | soft_rst1)
    pex_xor = 1'b0
/;
foreach (qw/nvus_cpu pexs roms/) {
    new_assigns "rpop_$_ = rvalid_$_ && rlast_$_ && rready_$_";
    new_assigns "bpop_$_ = bvalid_$_ && bready_$_";
}

# USER for TCMS access
new_codes q@
    assign aruser_cpum0[2:0] = (araddr_cpum0[23:20] == 4'h2) ? 3'b000 :         // ITCM0
                               (araddr_cpum0[23:20] == 4'h3) ? 3'b001 :         // DTCM0
                               (araddr_cpum0[23:20] == 4'h4) ? 3'b010 : 3'b011; // I/DTCM1
    assign awuser_cpum0[2:0] = (awaddr_cpum0[23:20] == 4'h2) ? 3'b000 :
                               (awaddr_cpum0[23:20] == 4'h3) ? 3'b001 :
                               (awaddr_cpum0[23:20] == 4'h4) ? 3'b010 : 3'b011;

    assign aruser_pexm[2:0]  = (araddr_pexm[23:20] == 4'hA) ? 3'b000 :         // ITCM0
                               (araddr_pexm[23:20] == 4'hB) ? 3'b001 :         // DTCM0
                               (araddr_pexm[23:20] == 4'hC) ? 3'b010 : 3'b011; // I/DTCM1
    assign awuser_pexm[2:0]  = (awaddr_pexm[23:20] == 4'hA) ? 3'b000 :
                               (awaddr_pexm[23:20] == 4'hB) ? 3'b001 :
                               (awaddr_pexm[23:20] == 4'hC) ? 3'b010 : 3'b011;

    assign hauser_dapahb[2:0] = haddr_dapahb[22:20];  // 0-3
@;

### ID remap or extent
new_cell $nicname, "nic_i0";    # instance NIC to get ID bitwidth
my $inic = current_cell;        # prevent 'new_cell' overwrite current_cell
my $wide_idport = "";
for my $n (keys %idw) {
    my $nicw = $inic->_pins("awid_$n")->width;
    # need remap
    if ($nicw > $idw{$n}) {
        print "  > slave port '$n' need remap ( $nicw -> $idw{$n} )\n";
        my $clk = defined $clks{$n} ? $clks{$n} : 'clk_out1';
        new_cell "fbrc_id_remap_axi4", "id_remap_$n",
            {IW=>$nicw, OW=>$idw{$n}, DEPTH=>16};
        conn_pins qq/
            clk     # $clk
            rstn    # resetn
            a_*     # *_${n}_int
            b_*     # *_${n}
        /;
    }
    # simply expand
    elsif ($nicw < $idw{$n}) {
        print "  > slave port '$n' need expand ( $nicw -> $idw{$n} )\n";
        $wide_idport .= sprintf(" a?.id_%s[%0d:0]", $n, $idw{$n}-1);
    }
    # if equal , just use directly
    else {
        print "  > slave port '$n' have same bitwidth ( $nicw == $idw{$n} )\n";
    }
}


## ID gen
new_cell "fbrc_id_gen", "id_gen_eth_pex_cfg", {ETHID => 14, PEXID => 14};
conn_pins q/
    clk_out1                    # =
    axi_aclk                    # =
    resetn_*                    # resetn

    nic2eth_mac_a*(_int)?       # a*_eth_cfg_int    # in
    nic2eth_mac_*               # *_eth_cfg
    eth_mac2nic_*(_int)?        # *_eth_cfg_int     # out
    eth_mac2nic_*               # *_eth_cfg         # in

    nic2cpu_pex_ctrl_a*(_int)?  # a*_pex_cfg_int    # in
    nic2cpu_pex_ctrl_*          # *_pex_cfg
    cpu_pex_ctrl2nic_*(_int)?   # *_pex_cfg_int     # out
    cpu_pex_ctrl2nic_*          # *_pex_cfg         # in
/;

## NIC
current_cell "nic_i0";

def_output "hready_dapahb"; # prevent script swallow this signal

unuse_pins q/
    # AXI lite not used signals
    a.(size|burst|lock|cache|len|prot)_(eth|pex)_cfg
    wlast_(eth|pex)_cfg
    rlast_(eth|pex)_cfg#1

    # unsupport axi features
    pslverr_(?!dapapb)*         # dapabp support pslverr
    a?r*_msix                   # MSIX only write
    aw(lock|cache|prot)_msix wid_msix
    a.(lock|cache|prot)_pexs
/;

conn_pins q/
    nicclk              # clk_out1
    pexclk              # axi_aclk
    nicresetn           # resetn
    nicclken            # locked
    pexresetn           # resetn

    hready_dapahb       # hready_dapahb
    hreadyout_dapahb    # hready_dapahb
    hselx_dapahb        # 1

    a*size_(cpu*|tcms)  # =[1:0]            # # cpu size 2bits only
    pselx_*_cfg         # psel_*_cfg

    paddr_(nvu|rdm)_cfg # {_[11:0], paddr_$2_cfg[19:2], _[1:0]}
    paddr_cpureg        # =[19:0]
    a.addr_nvus_cpu     # =[23:0]
    a.addr_tcms         # =[21:0]

    # these prot will be scala
    a.prot_nvu*         # =[]

    # len currently only support 5 bits
    a.len_nvu*          # =[4:0]

    # ROMS not need write, we use AXI4 ID remap which dont support wid
    wid_roms            # =[11:0]

    # If there's _int net, it'll be used instead
    *                   # *(_int)
/;

# dont swallow these, due to ID gen/map
#def_port "bready_(?!.*_int$).*"; # all bready_* except end with _int
def_port "[br]ready_*"; # all bready_* & rready_*
def_port "paddr_(nvu|rdm)_cfg[31:0] a.addr_nvus_cpu[63:0] a.addr_tcms[31:0]";
def_port $wide_idport;

#@ # debug probe
#@ new_cell "fbrc_nicv2_dbg", "fbrc_nicv2_dbg_i0";
#@ conn_pins q/
#@     cpu_pex_ctrl2nic_*   # *_pex_cfg
#@ 
#@     nic2cpu_pex_a*ready  # a*ready_pexm
#@     nic2cpu_pex_wready   # wready_pexm
#@     cpu_pex2nic_bready   # bready_pexm
#@     cpu_pex2nic_rready   # rready_pexm
#@ 
#@     cpu_pex2nic_awready  # awready_pexs
#@     cpu_pex2nic_wready   # wready_pexs
#@     nic2cpu_pex_bready   # bready_pexs
#@     nic2cpu_pex_rready   # rready_pexs
#@ 
#@     cpu_pex2nic_a*       # a*_pexm
#@     cpu_pex2nic_w*       # w*_pexm
#@     nic2cpu_pex_b*       # b*_pexm
#@     nic2cpu_pex_r*       # r*_pexm
#@ 
#@     nic2cpu_pex_a*       # a*_pexs
#@     nic2cpu_pex_w*       # w*_pexs
#@     cpu_pex2nic_b*       # b*_pexs
#@     cpu_pex2nic_r*       # r*_pexs
#@ 
#@     nvu2pex_mstr_axi_*   # *_nvus_pex
#@     nvu2cpu_mstr_axi_*   # *_nvus_cpu
#@     nic2eth_mac_*        # *_eth_cfg
#@     eth_mac2nic_*        # *_eth_cfg
#@     apb2rdm_*            # *_rdm_cfg
#@     rdm2apb_*            # *_rdm_cfg
#@     apb2nvu_*            # *_nvu_cfg
#@     nvu2apb_*            # *_nvu_cfg
#@ 
#@     *  | =
#@ /;

write_verilog;


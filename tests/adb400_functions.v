//-----------------------------------------------------------------------------
// The confidential and proprietary information contained in this file may
// only be used by a person authorised under and to the extent permitted
// by a subsisting licensing agreement from ARM Limited.
//
// (C) COPYRIGHT 2011-2012 ARM Limited.
// ALL RIGHTS RESERVED
//
// This entire notice must be reproduced on all copies of this file
// and copies of this file may only be made by a person if such person is
// permitted to do so under the terms of a subsisting license agreement
// from ARM Limited.
//
// Checked In :  2012-10-19 17:50:19 +0100 (Fri, 19 Oct 2012)
// Revision : 137895
//
// Release Information : PL405-r2p0-00rel0
//
//-----------------------------------------------------------------------------
// Verilog-2001 (IEEE Std 1364-2001)
//-----------------------------------------------------------------------------
// File: adb400_functions.v
//-----------------------------------------------------------------------------
// Purpose : Commonly used functions to include.
//-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // Not actually a clogb2 function (does not return strictly the ceiling of log2(x)),
  // instead it is returns the number of bits required to represetn the argument.
  //-----------------------------------------------------------------------------
  function integer clogb2 (input integer x);
    begin : fn_clogb2
      for (clogb2 = 0 ; ((x >> clogb2) > 0) ; clogb2 = clogb2 + 1) begin end
    end
  endfunction // clogb2


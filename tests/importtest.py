


print("outside " + __name__)

class tt(object):
  def __init__(self, i):
    print("inside tt : %s = %s %s" % (__name__, i, type(self)))


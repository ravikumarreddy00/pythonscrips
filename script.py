#!/usr/bin/python
total = 0;
def sum(arg1,arg2):
  total = arg1 + arg2
  print "Inside the function: %s" %total
  return total;
sum(10,20);
print "Outside the function: %s" %total

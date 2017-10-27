#!/usr/bin/python
def changeme(mylist):
  mylist = [1,2,3,4];
  print "values inside the function %s:" % mylist
  return;
mylist = [10,20,30];
changeme(mylist);
print "values outside the function %s:" % mylist


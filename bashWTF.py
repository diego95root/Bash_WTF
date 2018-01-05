#!/usr/bin/python
import sys

intro = """a() { /???/???/p????f ${@};}; o() { a ${#};}; a $(a "\\\\\\\\"""
addings = """"""
semistart =  """"; a "\\\\\\\\"""
end = """");"""

try:
    arg1 = sys.argv[1]
except IndexError:
    print "Provide the message you want to encode as an argument"
    sys.exit()

for i in range(0, len(arg1)):
    nums = list(str(int(oct(int(hex(ord(arg1[i])),16)))))
    addin = ""
    for each in nums:
        n = """ "" """*int(each)
        base = "`o {}`".format(n)
        addin += base
    addings += addin
    if i != len(arg1)-1: addings += semistart

print "Insert this code in a linux / OS X terminal:\n-----------------\n", intro + addings + end, "\n-----------------"

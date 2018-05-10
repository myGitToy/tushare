# -*- coding: utf-8 -*-
import re
print "hello cloud9"
s="qiaoh@shanghai-air.com"
print "this E-mail address has",len(s),"numbers!"
name=re.match(r'^([0-9a-zA-Z]+)@([0-9a-zA-Z\-]+.[a-zA-Z]+)$',s)
print "User Name:",name.group(1)
print "Company Name:",name.group(2)
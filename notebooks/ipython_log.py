# IPython log file

import re
c = re.compile(r'\d{2}/\d{2}/\(?<ano>\d{4})')
get_ipython().magic(u'pinfo c')
import re
c = re.compile(r'\d{2}/\d{2}/\(?P<ano>\d{4})')
get_ipython().magic(u'pinfo c')
import re
c = re.compile(r'\d{2}/\d{2}/\(?P<ano>(\d{4}))')
get_ipython().magic(u'pinfo c')
import re
c = re.compile(r'\d{2}/\d{2}/\(?P<ano>\d{4})')
import re
c = re.compile(r'\d{2}\d{2}\(?P<ano>\d{4})')
import re
c = re.compile(r'\d{2}/\d{2}/(?P<ano>\d{4})')
import re
c = re.compile(r'\d{2}/\d{2}/(?P<ano>\d{4})')
get_ipython().magic(u'pinfo c')
get_ipython().magic(u'pinfo2 c')
def oi(nome="Abelardo Mota"):
    
    return "oi %(nome)s" % {'nome': nome}
oi('juliana')
get_ipython().magic(u'pinfo oi')
get_ipython().magic(u'pinfo2 oi')
def oi(nome="Abelardo Mota"):
    
    return "oi %(nome)s" % {'nome': nome}

get_ipython().magic(u'pinfo2 oi')
import numpy as np
get_ipython().magic(u'psearch np.*load*')
get_ipython().magic(u'magic')
get_ipython().magic(u'commads')
get_ipython().run_cell_magic(u'file', u"'run.py'", u"\ndef hehe():\n    \n    return 'hehe'")
get_ipython().magic(u'run run.py')
get_ipython().run_cell_magic(u'file', u"'run.py'", u"\ndef hehe():\n    \n    return 'hehe'\n\nhehe()")
get_ipython().magic(u'run run.py')
get_ipython().run_cell_magic(u'file', u"'run.py'", u"\ndef hehe():\n    \n    return 'hehe'\n\nprint hehe()")
get_ipython().magic(u'run run.py')
get_ipython().run_cell_magic(u'file', u"'run_a.py'", u'\ndef hehe_a():\n    \n    return a\n\nprint hehe_a()')
get_ipython().magic(u'run run_a.py')
a = 'meu nome'
get_ipython().magic(u'run -i run_a.py')
get_ipython().magic(u'paste')
get_ipython().magic(u'cpaste')
get_ipython().magic(u'prun run.py')
def print_1_10():
    
    for i in xrange(1, 11):
        
        print i
        
get_ipython().magic(u'prun print_1_10()')
get_ipython().magic(u'time print_1_10()')
def power():
    
    for i in xrange(100):
        
        x = i**2
        
get_ipython().magic(u'time power()')
def power():
    
    for i in xrange(1000):
        
        x = i**2
        
get_ipython().magic(u'time power()')
def power():
    
    for i in xrange(10000):
        
        x = i**2
        
get_ipython().magic(u'time power()')
def power():
    
    for i in xrange(100000):
        
        x = i**2
        
get_ipython().magic(u'time power()')
get_ipython().magic(u'timeit power()')
get_ipython().run_cell_magic(u'time', u'', u'\nfor i in xrange(100000):\n    \n    x = i**3')
get_ipython().run_cell_magic(u'timeit', u'', u'\nfor i in xrange(1000):\n    \n    x = i**2')
get_ipython().magic(u'who')
get_ipython().magic(u'whois')
get_ipython().magic(u'whos')
get_ipython().magic(u'who_ls')
for x in %who_ls:
    
    exec(x)
for $x in %who_ls:
    
    exec(x)
a = get_ipython().magic(u'who_ls')
for x in a:
    
    print x
for x in a:
    
    print typeof x
for x in a:
    
    print x.__class__
a = get_ipython().magic(u'who')
for x in a:
    
    print x.__class__
logging
get_ipython().magic(u'logstart')
get_ipython().system(u'ls')
get_ipython().system(u'dir')
get_ipython().system(u'mkdir')
dirname = 'ch03_pasta'
get_ipython().system(u'mkdir $dirname')
get_ipython().magic(u'lprun')
get_ipython().magic(u'load_ext line_profiler')
get_ipython().magic(u'load_ext line_profiler')
def add_and_power(x, y):
    
    added = x + y
    power = x**y
    
    return added, power
get_ipython().magic(u'lprun -f add_and_power add_and_power(2,3)')
[IPython coockbook](https://github.com/ipython/ipython/wiki/Cookbook%3A-Index)

#!/usr/bin/python2


import sys

sys.path.append("../PyUserInput/") 
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

if sys.argv[1] == "move":
    m.move(sys.argv[2], sys.argv[3])
if sys.argv[1] == "click":
    m.click(sys.argv[2], sys.argv[3])

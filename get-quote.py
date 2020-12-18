# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:27:53 2020

@author: yasuo
"""

import random

last=13

f = open("quotes.txt")
quotes = f.readlines()
f.close()

rdn = random.randint(0,last)


print(quotes[rdn])
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:53:08 2017

@author: e
just a way to ensure that all functions in maputils are working
"""
import maputils as mu
mu.phelp = []
a = mu.Map(11, 6)
for row in a:
    for cell in row:
      cell.display = "="
b = a[4][5]

b.setneighborhood(0, 1, a)
for row in b.neighborhood:
    for cell in row:
        cell.display=")"


b.display = "+"
mu.prettyprint(a)

    
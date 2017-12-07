# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:53:08 2017

@author: e
just a way to ensure that all functions in maputils are working
"""
import maputils as mu

a = mu.createmap(20, 20)
for row in a:
    for cell in row:
        cell.display = "="
b = a[2][2]

b.setneighborhood(1, 4, a)
for row in b.neighborhood:
    for cell in row:
        cell.display=")"

b.display = "+"
mu.prettyprint(a)

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:53:08 2017

@author: e
just a way to ensure that all functions in maputils are working
"""
import maputils as mu
mu.phelp = []
mu.cells = [["mountain", "M"]]
try:
    a = mu.Map(12, 34)
    for row in a:
        for cell in row:
            cell.display = "="
        b = a[8][11]
            
        b.setneighborhood(0, 2, a)
        for row in b.neighborhood:
            for cell in row:
                cell.display=")"

    b.display = "+"
    mu.prettyprint(a)
except:
    raise
    
    
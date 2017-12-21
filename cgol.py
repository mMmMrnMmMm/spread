# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:16:40 2017

@author: e
an attempt at a conway's game of life implementation. 
"""
import maputils as mu
import argparse, random
#argparse code
mu.phelp = ["type 'quit to exit",
            "type 'next' to advance the simulation",
            "type 'print' to print the current state"]
mu.cells = [["dead", "#"],
            ["alive", "*"]
    ]
args = False
if args == False:
    width = int(input("what do you want the width of the grid to be?"))
    height = int(input("what do you want the height of the grid to be?"))
birth = [3]
life =[2,3]
grid = mu.Map(height, width)
living = random.sample(grid.cells, int(grid.height*grid.width/2))
for cell in grid.cells:
    cell.setneighborhood(0, 1, grid)
    cell.adj = 0
for cell in living:
    cell.changetype(1)

mu.prettyprint(grid)
run = True

while run == True:
    for cell in living:
        for part in cell.neighborhood:
            for acell in part:
                acell.adj += 1
        cell.adj -= 1
    
    for cell in grid.cells:
        if cell.name == "dead":
            if cell.adj in birth:
                cell.changetype(1)
        if cell.name == "alive":
            if cell.adj not in life:
                cell.changetype(0)
        #cell.display = str(cell.adj)
        cell.adj = 0
                
    nxt = input("what now?")[0].lower()
    if nxt == "p":
        mu.prettyprint(grid)
    elif nxt == "q":
        run = False
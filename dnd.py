import random
import maputils as mu


mu.cells = [["empty", " "],
         ["mountain", "Λ"],
         ["water","~"],
         [],
         []]

mapheight = 8
mapwidth = 4
    
Map = mu.createmap(mapwidth, mapheight)

def wgen(m):
    #elevation
    #0000+00000+  - 11*5 = 55/10 = 5 = 5
    #0+000000000
    #0000000+000
    #00+00000000
    #00000000000
    for i in range(random.randint(1,mapheight*mapwidth/10)):
        pass

mu.phelp = []
mu.prettyprint(Map)

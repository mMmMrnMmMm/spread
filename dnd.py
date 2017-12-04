import random
import test as mu


mu.cells = [["empty", " "],
         ["mountain", "Λ"],
         ["water","~"],
         [],
         []]

mapheight = 8
mapwidth = 4
def wgen(m):
    #elevation
    #0000+00000+  - 11*5 = 55/10 = 5 = 5
    #0+000000000
    #0000000+000
    #00+00000000
    #00000000000
    for i in range(random.randint(1,mapheight*mapwidth/10)):
        pass
    
Map = mu.createmap(mapwidth, mapheight)
mu.phelp = []
mu.prettyprint(Map)

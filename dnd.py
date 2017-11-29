import test as mu

mu.cells = [["empty", " "],
         ["mountain", "Λ"],
         ["water","~"],
         [],
         []]

Map = mu.createmap(4, 3)
mu.phelp = []
mu.prettyprint(Map)

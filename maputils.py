phelp = ["h to hide help ", "i j k l for movement "]
cells = [["empty", " "]
        ]

from math import sqrt, floor
# 1 8 7
# 2 0 6
# 3 4 5
#==============================================================================
# class cell():
#     def celcheck(self,cel_id):
#         if type(cel_id) == str:
#             cel = cells.index(cel_id)
#         else:
#             cel = cel_id
#         return cel
#     def __init__(self, cel_id, x, y):
#         cel = self.celcheck(cel_id)
#         self.name = cells[cel][0]
#         self.display = cells[cel][1]
#         self.contents = []
#         self.submap = []
#         self.state = 0
#         self.x = x
#         self.y = y
#     def changetype(self, typ):
#         self.name = cells[self.celcheck(typ)][0]
#         self.display = cells[self.celcheck(typ)][1]
#     def setneighborhood(self, typ, size, context):
#         self.neighborhood = []
#         if typ == 0 or typ == "square":
#             self.neighborhood = [[context[i%context.height][j%context.width] 
#             for j in range(self.x-size, size+self.x+1)] 
#             for i in range(self.y-size, size+self.y+1)]
# 
# class Map:
#     def __init__(self, height, width, parent = None):
#         self.contents = [[cell(0, j, i) for j in range(width)] for i in range(height)]
#         self.parent = parent
#         self.height = height
#         self.width = width
#         self.cells = [self.contents[i%height][i%width] for i in range(width*height)]
#     def __getitem__(self, key):
#         return self.contents[key]
#     def __len__(self):
#         return len(self.contents)
#==============================================================================

class cell():
    def __init__(self):
        pass
    def changetype(self):
        pass
    def addneighborhood(self):
        pass

class Map():
    def __init__(self, width, height, parent = None):
        self.parent = parent
        self.contents = [[cell for j in range(width)] for i in range(height)]
        self.height = height
        self.width = width
        self.celllist = []
    def __getitem__(self, key):
        """
        takes in a tuple for the x, y values. 
        """
        return self.contents[key[0]][key[1]]
    def __len__(self):
        return self.height*self.width

def prettyprint(Map):
    printhelp = phelp
    while len(printhelp) < len(Map):
        printhelp.append(" ")
    printstr = ""
    for i in range(len(Map)):
        for j in Map[i]:
            printstr = printstr+j.display
        printstr = printstr+ "    "+ printhelp[i]+"\n"
    print(printstr)
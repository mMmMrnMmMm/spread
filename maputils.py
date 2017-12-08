phelp = ["h to hide help \n", "i j k l for movement \n"]
cells = [["empty", " "]
        ]

from math import sqrt
# 1 8 7
# 2 0 6
# 3 4 5
class cell():
    def celcheck(self,cel_id):
        if type(cel_id) == str:
            cel = cells.index(cel_id)
        else:
            cel = cel_id
        return cel
    def __init__(self, cel_id, x, y):
        cel = self.celcheck(cel_id)
        self.name = cells[cel][0]
        self.display = cells[cel][1]
        self.contents = []
        self.submap = []
        self.state = 0
        self.x = x
        self.y = y
    def changetype(self, typ):
        self.name = cells[typ][0]
        self.display = cells[typ][1]
    def setneighborhood(self, typ, size, context):
        if typ == 0 or typ == "square":
            self.neighborhood = []
            for j in range(self.x - size, self.x + size+1):
                self.neighborhood.append([])
                for i in range(self.y - size, self.y + size+1):
                    self.neighborhood[len(self.neighborhood)-1].append(
                            context[i%len(context)][j%len(context)])
        elif typ == 1 or typ == "circle":
            self.neighborhood = [
                    [context[i][j] for j in range(self.x-size, size+self.x+1) 
                    if size > sqrt(abs(j - self.x)^2 + abs(i - self.y)^2) ] 
                    for i in range(self.y-size, size+self.y+1)]

            

def fillcell(x, y): #needs work
    return cell(0, x, y)

def createmap(x,y, cellgen = fillcell):
    return [[cellgen(x = i, y = j) for i in range(x)] for j in range(y)]

def prettyprint(Map):
    printhelp = phelp
    while len(printhelp) < len(Map):
        printhelp.append("\n")
    printstr = ""
    for i in range(len(Map)):
        for j in Map[i]:
            printstr = printstr+j.display
        printstr = printstr+ "    "+ printhelp[i]
    print(printstr)
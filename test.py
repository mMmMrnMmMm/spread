phelp = ["h to hide help \n", "i j k l for movement \n"]
cells = [["empty", " "]
        ]
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
            self.neighborhood = [[] for i in range(size*2+1)]
            

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
phelp = ["h to hide help \n", "i j k l for movement \n"]
cells = [["empty", " "]
        ]

from math import sqrt, floor
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
        self.neighborhood = []
        if typ == 0 or typ == "square":
            for j in range(self.y - size, self.y + size+1):
                self.neighborhood.append([])
                for i in range(self.x - size, self.x + size+1):
                    self.neighborhood[len(self.neighborhood)-1].append(
                            context[j%len(context)][i%len(context[j])])
        elif typ == 1 or typ == "circle":
            for j in range(self.x - size, self.y + size +1):
                self.neighborhood.append([])
                for i in range(self.y - int(round(sqrt(abs(size^2 - j^2)))),
                                self.y + int(round(sqrt(abs(size+1^2 - j^2))))):
                    self.neighborhood[len(self.neighborhood)-1].append(
                            context[j%len(context)][i%len(context)])

class Map:
    def __init__(self, height, width):
        self.contents = [[cell(0, j, i) for j in range(width)] for i in range(height)]
    def __getitem__(self, key):
        return self.contents[key]
    def __len__(self):
        return len(self.contents)



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
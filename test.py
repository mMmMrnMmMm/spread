phelp = ["h to hide help \n", "i j k l for movement \n"]
cells = [["empty", " "]
        ]
# 1 8 7
# 2 0 6
# 3 4 5

class cell():
    def __init__(self, cel_id):
        if type(cel_id) == str:
            cel = cells.index(cel_id)
        else:
            cel = cel_id
        self.name = cells[cel][0]
        self.display = cells[cel][1]
        self.contents = []
        self.submap = []
        self.state = 0


def fillcell(): #needs work
    return cell(0)

def createmap(x,y, cellgen = fillcell()):
    return [[cellgen for i in range(x)] for j in range(y)]

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

                
            


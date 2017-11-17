phelp = ["h to hide help \n", "i j k l for movement \n"]
# 1 8 7
# 2 0 6
# 3 4 5
def fillcell(): #needs work
    return {"name":"empty", #cell name
            "display":"M", #what character it is displayed as
            "state":0,  #what the cell is currently displaying (0= self, 1 = contents, 2 = direction)
            "direction":0, #what direction it is pointing in
            "contents":[] #what items are on the cell
            }

class cell():
    def __init__(self, name, display):
        self.name
        self.display
        self.contents = []
        self.submap = []

def createmap(x,y):
    return [[fillcell() for i in range(x)] for j in range(y)]

def prettyprint(Map):
    printhelp = phelp
    while len(printhelp) < len(Map):
        printhelp.append("\n")
    printstr = ""
    for i in range(len(Map)):
        for j in Map[i]:
            printstr = printstr+j["display"]
        printstr = printstr+ "    "+ printhelp[i]
    print(printstr)

                
            


wmap = []
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

def createmap(x,y):
    Map = []
    width = []
    for i in range(x):
        width.append(fillcell())
    for i in range(y):
        Map.append(width)
    return Map

def prettyprint():
    printhelp = ["h to hide help \n", "i j k l for movement \n"]
    while len(printhelp) < len(wmap[0]):
        printhelp.append("\n")
    printstr = ""
    for i in range(len(wmap)-1):
        for j in wmap[i]:
            printstr = printstr+j["display"]
        printstr = printstr+ "    "+ printhelp[i]
    print(printstr)

def tick():
    nextmap =  createmap(len(wmap),len(wmap[0]))
    for y in len(wmap)-1:
        for x in len(wmap[0])-1:
            cell = wmap[y][x]
            if cell["name"] == "mine":
                pass
                
                

wmap = createmap(6,7)
prettyprint()


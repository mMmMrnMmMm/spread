wmap = []
# 1 8 7
# 2 0 6
# 3 4 5
def fillcell(): #needs work
    return {"name":"empty","display":" ","state":0, 
            "direction":0}

def createmap(x,y):
    Map = []
    width = []
    for i in range(y):
        width.append(fillcell())
    for i in range(x):
        Map.append(width)
    return Map

def prettyprint():
    printstr = ""
    for i in wmap:
        for j in i:
            printstr = printstr+j["display"]
        printstr = printstr+"\n"
    print(printstr)

def tick():
    nextmap =  createmap(len(wmap),len(wmap[0]))
        

wmap = createmap(6,7)
prettyprint()


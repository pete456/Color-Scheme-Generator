import sys
import color

def generatecomplementary(colorobj, amount=1):
    """Generates a list of complementary colors. Finds the proper angle to add to the colorobj hue based off the amount. Then creates color list based of new hues.
    """
    startHSV=colorobj.getHSV()
    angle=360/(amount+1)
    huelist=[startHSV[0]]
    rgblist=[]
    for colorint in range(amount):
        testangle=huelist[colorint]+angle
        if testangle > 360:
            testangle-=360
        huelist.append(testangle)

    for hue in huelist:
        testlist=[hue,startHSV[1],startHSV[2]]
        testcolor = color.Color(testlist)
        rgblist.append(color.Color(testlist))       
    return rgblist

def checkscheme(arglist, arg):
    """Returns index of arg in arglist or if not found returns -1.
    """
    return arglist.index(arg) if arg in arglist else -1

def printcolors(colorlist):
    """Prints the hex color value of color in colorlist.
    """
    for item in colorlist:
        print(item.getRGB())

colorschemelist=['s','t','a','c']

if len(sys.argv) < 3:
    print("Not enough arguments")
    exit()

index=checkscheme(colorschemelist,sys.argv[1][1:])
hex=sys.argv[len(sys.argv)-1]
inputcolor = color.Color(hex)

if index == -1:
    print("Incorrect arguments")
    exit()
elif index == 0:
    comp=generatecomplementary(inputcolor)[1]
    complist=[inputcolor,comp+30,comp-30]
elif index == 1:
    complist=generatecomplementary(inputcolor,2)
elif index == 2:
    complist=[inputcolor,inputcolor+30,inputcolor-30]
elif index == 3:
    complist=generatecomplementary(inputcolor)
    
printcolors(complist)

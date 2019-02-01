import color
from color import hsvtorgb

def generatecomplementary(Color, amount):
    startHSV=Color.getHSV()
    angle=360/(amount+1)
    huelist=[startHSV[0]]
    rgblist=[]
    for color in range(amount):
        testangle=huelist[color]+angle
        if testangle > 360:
            testangle-=360
        huelist.append(testangle)

    for hue in huelist:
        testlist=[hue,startHSV[1],startHSV[2]]
        rgblist.append(hsvtorgb(testlist))       
    return rgblist

testcolor = color.Color('edf636')
complement=generatecomplementary(testcolor,1)
print(complement)

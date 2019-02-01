import color

def generatecomplementary(Color, amount):
    startHSV=Color.getHSV()
    angle=360/(amount+1)
    huelist=[startHSV[0]]
    for color in range(amount):
        testangle=startHSV[0]+angle
        if testangle > 360:
            testangle-=360
        huelist.append(testangle)
    return huelist

testcolor = color.Color('0xadb45b')
hue=generatecomplementary(testcolor,1)
hsvlist=[hue[1],testcolor.getHSV()[1],testcolor.getHSV()[2]]
print(color.hsvtorgb(hsvlist))

    

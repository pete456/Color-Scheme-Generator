import math

class Color:
    def __init__(self,rgb):
        self.rgb=rgbtolist(rgb)

    def getRGB(self):
        """Return a hex string, without any identifiers
        """
        rgbstring=''
        for item in self.rgb:
            rgbstring+="{0:02X}".format(item)
        return rgbstring
    
    def getHSV(self):
        """Returns a dictionary with hue,sat(uration),val(ue)
        """
        fractionrgb=fractionizergb(self.rgb)
        hue=math.floor(calculatehue(fractionrgb))
        sat=calculatesaturation(fractionrgb)
        value=calculatevalue(fractionrgb)
        return {"hue":hue,"sat":sat,"val":value}
    
def fractionizergb(rgb):
    """Takes list of rgb values and divides them by 255.
    Returns new list of rgb values
    """
    fractionizedrgb=[]
    for i in range(3):
        value=rgb[i]/255
        fractionizedrgb.append(float("{0:.3f}".format(value)))
    return fractionizedrgb
   
def rgbtolist(rgb: str):
    """Converts a hex string to a list of independent R,G,B values.
    Returns list of RGB individual values
    """
    rgb = rgb[2:] if rgb [:2] == "0x" else rgb
    rgblist = [(int(rgb[2*color],16)*16** 1 + int(rgb[2*color+1],16)) for color in range(3)]
    return rgblist
    
def calculatechroma(rgblist):
    """Returns chroma value from rgblist
    """
    chroma = max(rgblist) - min(rgblist)
    return chroma

def calculatehue(rgblist):
    """Calculates the hue value from rgblist.
    If the color is gray it will return -1
    else it will return the angle that represent the hue on the HSV color circle
    """
    chroma=calculatechroma(rgblist)
    if chroma == 0:
        return -1
    highestrgbletter=['R','G','B'][rgblist.index(max(rgblist))]
    if highestrgbletter == 'R':
        hue = ((rgblist[1]-rgblist[2]) / chroma) % 6
    elif highestrgbletter == 'G':
        hue = ((rgblist[2] - rgblist[0]) / chroma) + 2
    else:
        hue = ((rgblist[0] - rgblist[1]) / chroma) + 4
    hue*=60
    return hue

def calculatevalue(rgblist):
    """Returns the value portion of HSV
    """
    return max(rgblist)

def calculatesaturation(rgblist):
    """Calculates the saturation portion of HSV
    """
    if calculatevalue(rgblist) == 0:
        return 0;
    else:
        return calculatechroma(rgblist)/(calculatevalue(rgblist))

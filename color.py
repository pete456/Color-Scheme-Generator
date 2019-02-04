import math

class NotRGBHexError(Exception):
    pass

class Color:
    def __init__(self,rgb):
        """Takes in a rgb hex value or a hsv list
        """
        if type(rgb) == str:
            self.rgb=rgbtolist(rgb)
            self.rgbfraction=fractionizergb(self)
        elif type(rgb) == list:
            self.rgb=hsvtorgb(rgb)
            self.rgbfraction=fractionizergb(self)
            
    def __add__(self,color):
        if type(color) == int:
            test = self.getHSV()
            test[0]+=color
            if test[0] > 360:
                test[0]-=360
            return Color(test)

    def __sub__(self,color):
        if type(color) == int:
            test = self.getHSV()
            test[0]-=color
            if test[0] < 0:
                test[0]+=360
            return Color(test)
        
    def getRGB(self):
        """Return a hex string, without any identifiers
        """
        rgbstring=''
        for item in self.rgb:
            item=int(item)
            if item < 0:
                item*=255
                item=int(item)
            rgbstring+="{0:02X}".format(item)
        return rgbstring
    
    def getHSV(self):
        """Returns a list [0] = hue, [1] = saturation, [2] = value
        """
        return [calculatehue(self),calculatesaturation(self),calculatevalue(self)]
    
def fractionizergb(color):
    """Takes color object and divided rgb list by 255.
    Returns new list of rgb values
    """
    fractionizedrgb = []
    for i in range(3):
        value = color.rgb[i]/255
        fractionizedrgb.append(float("{0:.3f}".format(value)))
        
    return fractionizedrgb
   
def rgbtolist(rgb: str):
    """Converts a hex string to a list of independent R,G,B values.
    Returns list of RGB individual values
    """
    if rgb[:2] == "0x":
        rgb = rgb[2:]
    elif rgb[:1] == "#":
        rgb = rgb[1:]
    
    if len(rgb) != 6:
        raise NotRGBHexError()
    
    rgb = rgb[2:] if rgb [:2] == "0x" else rgb
    rgblist = [(int(rgb[2*color],16)*16** 1 + int(rgb[2*color+1],16)) for color in range(3)]
    return rgblist
    
def calculatechroma(color):
    """Returns chroma value of color
    """
    chroma = max(color.rgbfraction) - min(color.rgbfraction)
    return chroma

def calculatehue(color):
    """Calculates the hue value of color.
    If the color is gray it will return -1
    else it will return the angle that represent the hue on the HSV color circle
    """
    chroma=calculatechroma(color)
    rgblist=color.rgbfraction
    if chroma == 0:
        return -1
    highestrgbletter=['R','G','B'][rgblist.index(max(rgblist))]
    if highestrgbletter == 'R':
        hue = ((rgblist[1]-rgblist[2]) / chroma) % 6
    elif highestrgbletter == 'G':
        hue = ((rgblist[2] - rgblist[0]) / chroma) + 2
    else:
        hue = ((rgblist[0] - rgblist[1]) / chroma) + 4
    hue *= 60
    return float("{0:.3f}".format(hue))

def calculatevalue(color):
    """Returns the value portion of HSV
    """
    return max(color.rgbfraction)

def calculatesaturation(color):
    """Calculates the saturation portion of HSV
    """
    rgblist=color.rgbfraction
    if calculatevalue(color) == 0:
        return 0;
    else:
        return calculatechroma(color)/(calculatevalue(color))
    
def hsvtorgb(hsvlist):
    """Converts a list of hsv values to rgb values
    returns list of rgb values
    """
    hsv = hsvlist
    hue = hsv[0] / 60
    chroma = hsv[1] * hsv[2]
    x=chroma*(1-abs(hue%2-1))
    
    if hsv[0] == -1:
        rgblist=[0,0,0]
    elif 0<=hue<=1:
        rgblist=[chroma,x,0]
    elif 1<hue<=2:
        rgblist=[x,chroma,0]
    elif 2<hue<=3:
        rgblist=[0,chroma,x]
    elif 3<hue<=4:
        rgblist=[0,x,chroma]
    elif 4<hue<=5:
        rgblist=[x,0,chroma]
    elif 5<hue<=6:
        rgblist=[chroma,0,x]
    m = hsv[2]-chroma
    rgb=[rgblist[0]+m,rgblist[1]+m,rgblist[2]+m]
    rgb=[round(item*255,2) for item in rgb]
    return rgb

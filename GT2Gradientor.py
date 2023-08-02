import os
import sys
import shutil

def PaintID():
    idp = input("Enter New Color ID: ").upper()
    if os.path.exists(dir + "//..//Colour" + idp):
        print("This Color ID already exists! Try a different one.")
        return PaintID()
    else:
        return idp

def Splitter(str, n):
    list = str.split(" ")
    list[2].removesuffix("\n")
    return int(list[n])

if len(sys.argv) != 2:
    print("Boowomp")
    sys.exit(2137)

dir=sys.argv[1]
if not os.path.exists(dir):
    print("Boowomp")
    sys.exit(2137)
else:
    idp = PaintID()
    r1 = float(input("Red Color Multiplier For Start Color: "))/255
    g1 = float(input("Green Color Multiplier For Start Color: "))/255
    b1 = float(input("Blue Color Multiplier For Start Color: "))/255
    r2 = float(input("Red Color Multiplier For End Color: "))/255
    g2 = float(input("Green Color Multiplier For End Color: "))/255
    b2 = float(input("Blue Color Multiplier For End Color: "))/255
    upad = float(input("Upper Gradient padding in %: "))
    lpad = float(input("Lower Gradient padding in %: "))
    newdir = dir + "//..//Colour" + idp
    shutil.copytree(dir, newdir)
    colors = []
    for i in range (16):
        if (os.path.exists(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") and os.path.exists(newdir + "//PaintMask" + f'{i:02d}' + ".pal")):
            with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") as f:
                pal = f.readlines()
            with open(newdir + "//PaintMask" + f'{i:02d}' + ".pal") as f:
                mask = f.readlines()
            for j in range (19):
                if (mask[j] == '248 248 248\n'):
                    if pal[j] not in colors:
                        colors.append(pal[j])
    colors = sorted(colors, key=lambda x: (Splitter(x,0) + Splitter(x,1) + Splitter(x,2))/3, reverse=1 )
    high = (Splitter(colors[0],0) + Splitter(colors[0],1) + Splitter(colors[0],2))/3
    low = (Splitter(colors[-1],0) + Splitter(colors[-1],1) + Splitter(colors[-1],2))/3
    highp = high - (0.01*upad*(high - low))
    lowp = low + (0.01*lpad*(high - low))
    print(high, low, highp, lowp, "\n")
    mults = []
    for c in colors:
        if (Splitter(c,0) + Splitter(c,1) + Splitter(c,2))/3 >= high - (0.01*upad*(high - low)):
            mults.append([r1, g1, b1])
        elif (Splitter(c,0) + Splitter(c,1) + Splitter(c,2))/3 <= low + (0.01*lpad*(high - low)):
            mults.append([r2, g2, b2])
        else:
            mults.append([r1*((Splitter(c,0) - lowp)/(highp - lowp)) + r2*((highp - Splitter(c,0))/(highp - lowp)) ,
                          g1*((Splitter(c,1) - lowp)/(highp - lowp)) + g2*((highp - Splitter(c,1))/(highp - lowp)),
                          b1*((Splitter(c,2) - lowp)/(highp - lowp)) + b2*((highp - Splitter(c,2))/(highp - lowp))])

    for i in range (16):
        if (os.path.exists(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") and os.path.exists(newdir + "//PaintMask" + f'{i:02d}' + ".pal")):
            with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") as f:
                pal = f.readlines()
            with open(newdir + "//PaintMask" + f'{i:02d}' + ".pal") as f:
                mask = f.readlines()
            for j in range (19):
                if (mask[j] == '248 248 248\n'):
                    idx = colors.index(pal[j])
                    nums = pal[j].split(" ")
                    nums[2].removesuffix("\n")
                    ints = [int(int(nums[0]) * mults[idx][0]), int(int(nums[1]) * mults[idx][1]), int(int(nums[2]) * mults[idx][2])]
                    for k in range (3):
                        if ints[k] > 255:
                            ints[k] = 255
                        if ints[k] < 0:
                            ints[k] = 0
                    pal[j] = str(ints[0]) + " " + str(ints[1]) + " " + str(ints[2]) + "\n"
            with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal","w") as f:
                f.writelines(pal)

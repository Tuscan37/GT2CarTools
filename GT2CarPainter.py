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

if len(sys.argv) != 2:
    print("Boowomp")
    sys.exit(2137)

dir=sys.argv[1]
if not os.path.exists(dir):
    print("Boowomp")
    sys.exit(2137)
else:
    idp = PaintID()
    r = float(input("Red Color Multiplier:"))/255
    g = float(input("Green Color Multiplier:"))/255
    b = float(input("Blue Color Multiplier:"))/255
    newdir = dir + "//..//Colour" + idp
    shutil.copytree(dir, newdir)
    for i in range (16):
        if (os.path.exists(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") and os.path.exists(newdir + "//PaintMask" + f'{i:02d}' + ".pal")):
            with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal") as f:
                pal = f.readlines()
            with open(newdir + "//PaintMask" + f'{i:02d}' + ".pal") as f:
                mask = f.readlines()
            for j in range (19):
                if (mask[j] == '248 248 248\n'):
                    nums = pal[j].split(" ")
                    nums[2].removesuffix("\n")
                    ints = [int(int(nums[0]) * r), int(int(nums[1]) * g), int(int(nums[2]) * b)]
                    for k in range (3):
                        if ints[k] > 255:
                            ints[k] = 255
                        if ints[k] < 0:
                            ints[k] = 0
                    pal[j] = str(ints[0]) + " " + str(ints[1]) + " " + str(ints[2]) + "\n"
                    with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal","w") as f:
                        f.writelines(pal)


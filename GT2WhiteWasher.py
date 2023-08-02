import os
import shutil
import sys

if len(sys.argv) != 2:
    print("Boowomp")
    sys.exit(2137)

def PaintID():
    idp = input("Enter New Color ID: ").upper()
    if os.path.exists(dir + "//..//Colour" + idp):
        print("This Color ID already exists! Try a different one.")
        return PaintID()
    else:
        return idp

def Mode():
    mode = int(input("Select Grayscale Mode:\n0 - Average\n1 - Brightest of Three\n"))
    if mode < 0 or mode > 1:
        print("Try again! This time choose either 0 or 1!")
        return Mode()
    else:
        return mode

dir=sys.argv[1]

if not os.path.exists(dir):
    print("Boowomp")
    quit(2137)
else:
    idp = PaintID()
    newdir = dir + "//..//Colour" + idp
    m = float(input("Grayscale Multiplier:"))
    a = float(input("Grayscale Additive:"))
    mode = Mode()
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
                    if mode == 0:
                        avg = int((int(nums[0]) + int(nums[1]) + int(nums[2]))/3)
                        ints = [int(avg * m + a), int(avg * m + a), int(avg * m + a)]
                    if mode == 1:
                        ints = [int(nums[0]), int(nums[1]), int(nums[2])]
                        brightest = ints[0]
                        if ints[1] > brightest:
                            brightest = ints[1]
                        if ints[2] > brightest:
                            brightest = ints[2]
                        ints = [int(brightest * m + a), int(brightest * m + a), int(brightest * m + a)]
                    for k in range (3):
                        if ints[k] > 255:
                            ints[k] = 255
                        if ints[k] < 0:
                            ints[k] = 0
                    pal[j] = str(ints[0]) + " " + str(ints[1]) + " " + str(ints[2]) + "\n"
                    with open(newdir + "//ColourPalette" + f'{i:02d}' + ".pal","w") as f:
                        f.writelines(pal)


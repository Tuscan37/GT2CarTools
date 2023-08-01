import os
import sys

if len(sys.argv) != 2:
    print("Boowomp")
    sys.exit(2137)

dir=sys.argv[1]
if not os.path.exists(dir):
    print("Boowomp")
    sys.exit(2137)
else:
    r = float(input("Red Color Multiplier:"))/255
    g = float(input("Green Color Multiplier:"))/255
    b = float(input("Blue Color Multiplier:"))/255
    for i in range (16):
        if (os.path.exists(dir + "//ColourPalette" + f'{i:02d}' + ".pal") and os.path.exists(dir + "//PaintMask" + f'{i:02d}' + ".pal")):
            with open(dir + "//ColourPalette" + f'{i:02d}' + ".pal") as f:
                pal = f.readlines()
            with open(dir + "//PaintMask" + f'{i:02d}' + ".pal") as f:
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
                    with open(dir + "//ColourPalette" + f'{i:02d}' + ".pal","w") as f:
                        f.writelines(pal)


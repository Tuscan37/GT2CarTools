GT2PaintEditor and GT2WhiteWasher by Tuscan37

1. GT2PaintEditor

Usage: python3 GT2PaintEditor.py path/to/white/color

After a successful launch, input a new ID, three color components, for example: 
Enter New Color ID: 6A
Red Color Multiplier: 0
Green Color Multiplier:161
Blue Color Multiplier: 255

The program will only affect colors with the paintmask colors equal 248 248 248.

2. GT2WhiteWasher

Usage: python3 GT2WhiteWasher.py path/to/non-white/color

After a successful launch, input a new ID, grayscale multiplier, grayscale additive and grayscale mode.
There are two grayscale modes:
Component average
Brightest of the three components

How to find the right values:
Pick the brightest paint color in the car texture, for example (Jaguar XJ15): 32 121 155
Average mode (excluding multiplier and additive) will turn that color into 102 102 102.
Brightest of Three mode (excluding multiplier and additive) will turn that color into 155 155 155.
Let's say g is 155 which is your brightest gray color
m is the multiplier you chose
a is the additive
Your goal is to make sure g*m+a is equal or very slightly below 255. Play around with values to achieve the best results.

Usage example:
Grayscale Multiplier: 1.3
Grayscale Additive: 96
Select Grayscale Mode:
0 - Average
1 - Brightest of Three
1

The program will only affect colors with the paintmask colors equal 248 248 248.

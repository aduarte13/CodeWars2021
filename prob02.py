# Write a program to calculate the volume of a
# pizza given its height and radius on a single line.
# Round to nearest hundredth.
import math

# example inputs:
# 16.50 24.00
# 1.00 7.50

# example outputs:
# 29857.70 cubic inches
# 176.71 cubic inches

string = input()  # take input from console
string.split()    # delimit
height = float(string.split()[0])
radius = float(string.split()[1])

# formula:
# V = π * r * r * h (π = 3.1415926536)
volume = math.pi * radius * radius * height
volume = round(volume, 2)

print("%.2f cubic inches" % volume)

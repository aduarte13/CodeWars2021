"""
Having conquered the world of extreme underwater basket weaving, you
are now moving on to Xtreme Surface Skiing! As the most extremely
experienced X-games competitor in your new league, they are seeking
your expertise to decide what materials to use for the first round of
competitions (before the shark jumping round).

You will receive on a single line a SKI MATERIAL ("X" coordinate in table
below, A.K.A. the top row), followed by a skiing SURFACE ("Y" coordinate
in table below, A.K.A. the first column). Use the material-to-surface lookup
table in the discussion section to determine the coefficient of friction for the
given ski material on the given surface. Use that coefficient of friction to
find the minimum slope angle (using the inverse tangent (known as
arctan)) the league would need to use for the competition.

EXAMPLES:
    INPUT: WOOD RUBBER
    OUTPUT: 0.80 38.7

    INPUT: RUBBER RUBBER
    OUTPUT: 1.15 49.0

    INPUT: STEEL ICE
    OUTPUT: 0.03 1.7
"""
import math

surface_list = ("CONCRETE", "WOOD", "STEEL", "RUBBER", "ICE")
material_list = ("RUBBER", "WOOD", "STEEL")
"""
SURFACE    SKI MATERIAL
         RUBBER WOOD STEEL
CONCRETE 0.90  0.62  0.57
WOOD     0.80  0.42  0.30
STEEL    0.70  0.30  0.74
RUBBER   1.15  0.80  0.70
ICE      0.15  0.05  0.03
"""
surface_material_table = ((0.90, 0.62, 0.57),
                          (0.80, 0.42, 0.30),
                          (0.70, 0.30, 0.74),
                          (1.15, 0.80, 0.70),
                          (0.15, 0.05, 0.03))

file = open("input.txt", 'r')       # open file in read mode
raw_input = file.readline()
ski_material = raw_input.split(" ")[0]
surface = raw_input.split(" ")[1]

surface_index = surface_list.index(surface)
material_index = material_list.index(ski_material)

coefficient = surface_material_table[surface_index][material_index]
min_angle = math.atan(coefficient)
print('{0:.2f}'.format(coefficient) + " " + str(round(math.degrees(min_angle), 1)))

file.close()

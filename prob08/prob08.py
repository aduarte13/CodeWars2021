"""
King Candy has ordered Sour Bill, Wynnchel
and Duncan to build candy walls to slow down
Ralph -- who is on the way to the castle to
save Vanellope.
Ralph is angry. The angrier Ralph is, the
harder he hits!
Show Vanellope what she will see outside the
window in her cell as Ralph rushes to save
her.

Input
You will receive three integers, separated by spaces.
The first integer tells you how tall (max height of 40) the
candy wall is (use the hash character (#) to show walls).
The second integer tells you how high Ralph punches.
The third integer tells you how mad Ralph is on a scale of 1 to 99,
where 1 is annoyed someone is talking on their
phone, and 99 is strong enough to destroy the arcade.

Output
Show the aftermath of Ralph punching the wall.
Every 10 levels of angry will cause the destruction of the wall to
be one additional block more violent. At anger level 1 the wall will
fall down right next to where it was standing. At level 21 the wall
will get knocked 2 spaces away from where the wall was standing before it falls over.
(Use a period to show the spaces between the original wall, and the fallen wall)
The part of the wall below where Ralph punches will remain unchanged. If Ralph is
so angry he misses, the second integer will be zero (to show a miss) --
in that case, simply show the wall unharmed. Ralph can also miss by punching higher
than the wall is tall. Ralph is too tall to punch block number 1.

Discussion
Taking the example from above, let's break it down into before and after pictures.
The wall before it is punched should be 6 "blocks" tall. Then Ralph hits it at block-height 3,
with an anger-force of 11. From 0-9 the wall should just topple over to the right where it is hit.
At 10, 20, 30 ... 90, we need to add an additional period between the remainder of the wall Ralph
didn't punch, and the start of the toppled over wall on the ground. Since Ralph hits with a force
of 11, that means we crossed the 10-threshold, so we need to add one period after the wall before
we start scattering blocks on the ground.

EXAMPLES:
    INPUT 1:
    6 3 11
    OUTPUT 1:
    #
    #.####

    INPUT 2:
    4 2 9
    OUTPUT 2:
    ####

    INPUT 3:
    5 0 99
    OUTPUT 3:
    #
    #
    #
    #
    #

    INPUT 4:
    3 2 39
    OUTPUT 4:
    #...##

    INPUT: 5
    7 8 20
    OUTPUT 5:
    #
    #
    #
    #
    #
    #
    #
"""

file = open("input.txt", 'r')  # open file in read mode
raw_input = file.readline().split(" ")
wall_starting_height = int(raw_input[0])
hit_block_height = int(raw_input[1])
anger_force = int(raw_input[2])

# if too angery or hit misses, print the wall at starting height
if anger_force == 0 or (hit_block_height <= 1 or hit_block_height > wall_starting_height):
    for i in range(wall_starting_height):
        print('#')
else:
    # print still standing part of the wall
    wall_end_height = hit_block_height - 1
    for i in range(wall_end_height - 1):
        print('#')
    print('#', end='')

    # print distance periods
    distance = int(anger_force / 10)
    for i in range(distance):
        print('.', end='')

    # print knocked over part of wall
    fallen_wall_length = wall_starting_height - wall_end_height
    for i in range(fallen_wall_length):
        print('#', end='')

file.close()

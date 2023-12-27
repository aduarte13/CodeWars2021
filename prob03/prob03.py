# Ace Ventura, Pet Detective, is on the hunt for a rare albino
# pigeon. Help Ace find the pigeon with your drone's new
# mapping app.

# Input:
# You will receive a map grid made up of lines of ASCII
# characters. The map will be between 5-40 lines tall, and 5-80
# characters wide. Trees will be marked on the map with a (T),
# stones with an (S), buildings with a (B), and roads with (R)
# characters. The pigeon, if the drone can spot it, will be
# marked with a (P). All other empty spaces on the map will be
# marked with a period (.)
# ....R...............
# ....R.T........BB...
# ....R.T........BB...
# .S..R...............
# ....R.T........BB...
# ....R.T........BB.P.
# ....R...............
# ....RRRRRRRRRRRRRRRR

# Output
# If the drone marked the map with a (P) character, quickly tell Ace where the pigeon is by texting him the
# coordinates from the map. The upper left of the map will be (X=0,Y=0). The lower right of the map will be the
# maximum values for X and Y. If the drone couldn't spot the pigeon on the map, text Ace to try another map (see
# below).
# Ace, move fast, pigeon is at (18,5)
# Output the full sentence exactly as shown with only the map coordinates changing if your output found a pigeon.
# Else, output the sentence:
# No pigeon, try another map, Ace

file = open("input.txt", 'r')
lines = file.readlines()

for line in lines:
    for char in line:
        print(char)

file.close()



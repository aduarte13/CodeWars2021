"""
Joe Gardner teaches a music class at a school and needs your help. He is in need of some noise canceling
headphones to prevent headaches during some of his classes. Joe doesn't want to buy the headphones because
he wants to custom make them into some of his clothes so that his students won't know. Could you help Joe by
inverting (flip) the sound wave that is coming into the headset?

You will receive the number of lines you will receive followed by #'s in a wave pattern.
Note, there are no flat parts to the waves. Max Size of the wave is 80x80.

EX INPUT:
7
   #
  # #         #
 #   #       # #   #
#     #     #   # #
       #   #     #
        # #
         #
EX OUTPUT:
         #
        # #
       #   #     #
#     #     #   # #
 #   #       # #   #
  # #         #
   #
"""
file = open("input.txt", 'r')       # open file in read mode
lines = file.readlines()            # add file lines to str list

lines = lines[1:]                   # remove first line

for i in range(len(lines) - 1, -1, -1):             # count down from last index
    print(lines[i].replace("\n", ""))   # print line w/ newline removed

file.close()

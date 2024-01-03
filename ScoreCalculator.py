file = open("points.txt", 'r')      # open file in read mode
lines = file.readlines()
points_per_question = list()

question_count = int(input("Enter highest question solved: "))
total = 0

for i in range(question_count):
    if i != len(lines)-1:
        print(lines[i][:-1])
    else:
        print(lines[i])
    points = lines[i].split(" ")
    total += int(points[1][:-1])

print("score: " + str(total))

file.close()
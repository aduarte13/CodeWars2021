file = open("points.txt", 'r')      # open file in read mode
lines = file.readlines()
points_per_question = list()

question_count = int(input("Enter highest question solved: "))
total = 0

for i in range(question_count):
    print(lines[i].replace("\n", ""))
    points = lines[i].split(" ")
    total += int(points[1])

print("score: " + str(total))

file.close()
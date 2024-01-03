"""
Shang needs your help. His bosses just imposed
another rule on who can enlist into the military.
He cannot have anyone under his command who
has the same birthday (day and month only)!
Can you please check through the list of
birthdays and tell him how many duplicate sets
there are?

Note: Multiple people with same birthday are
counted only once while counting duplicate sets.

The input will be in the format mm/dd/yyyy

Output should have the first line indicating the amount of doubles.
The next line should list the dates, without the year,
that are duplicates in the order they appeared in the list.
"""

file = open("input.txt", 'r')       # open file in read mode
lines = file.readlines()            # add file lines to str list
lines = lines[1:]                   # remove first line
duplicates = list()
dates_seen = set()

for line in lines:
    date = line.split("/")
    date = date[0] + "/" + date[1]      # removes year from date
    if date not in dates_seen:
        dates_seen.add(date)
    elif date in dates_seen and date not in duplicates:
        duplicates.append(date)

file.close()

print(str(len(duplicates)) + "\nduplicates: ", end="")
for date in duplicates:
    print(date, end=" ")
if len(duplicates) == 0:
    print("None")

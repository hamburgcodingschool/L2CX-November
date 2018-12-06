people = ["Inga", "Julez", "Theresa", "Helder"]

# highest = len(people[0])
# longestName = people[0]
#
# for name in people:
#     print(name)
#     print(len(name))
#
#     if len(name) > highest:
#         highest = len(name)
#         longestName = name
#
#
# print("--------------")
# print(longestName)

indexOfLongest = 0
counter = 0

for name in people:
    print(name)
    print(len(name))

    if len(name) > len(people[indexOfLongest]):
        indexOfLongest = counter

    counter = counter + 1

print("--------------")
print(people[indexOfLongest])
print(len(people[indexOfLongest]))

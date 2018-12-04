# for loops

agesArray = [7, 12, 15, 8, 3, 21, 17]

total = 0
highest = agesArray[0]
lowest = agesArray[0]

for age in agesArray:
    total = total + age
    # print(age)
    # print(total)
    # print("-------------")

    if age > highest:
        highest = age

    if age < lowest:
        lowest = age

avg = total / len(agesArray)

print("Total: {}".format(total))
print("Average: {}".format(avg))
print("Highest: {}".format(highest))
print("Lowest: {}".format(lowest))


# ages = [12, 45, 23, 1, 20, 91.3]
#
# print(ages)
#
# #removes object with value 20
# ages.remove(20)
#
# print(ages)

numbers = [8, 4, 10, 12, 5, 10, 10, 4, 6]

print(numbers)

newNumbers = []

for number in numbers:
    if number >= 5:
        newNumbers.append(number)

print(newNumbers)


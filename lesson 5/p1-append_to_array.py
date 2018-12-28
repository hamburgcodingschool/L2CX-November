# names = ["John", "Rita", "Frannie", "Seb"]
#
# print("Who is the 5th person?")
# name = input()
#
# names.append(name)

import random

numbers = []

for i in range(0, 1000):
    r = random.randint(1, 10)
    numbers.append(r)


counter = 0

for number in numbers:
    if number > 5:
        counter += 1 # counter = counter + 1

print(counter)

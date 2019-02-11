import random

#create MATRIX

myMatrix1 = []
for i in range(0, 4):
    numbers = []

    for j in range(0, 4):
        number = random.randint(0, 9)
        numbers.append(number)

    myMatrix1.append(numbers)

print(myMatrix1)

#print MATRIX

for array in myMatrix1:
    newLine = ""
    for value in array:
        newLine += str(value) + " "
    print("{}= {}".format(newLine, sum(array)))
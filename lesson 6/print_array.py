
someNumbers = [1, 12, 23, 34, 50]



#
# someText = ""
# for i in range(0, len(someNumbers)):
#     if i != 0:
#         someText += ", "
#     someNumber = someNumbers[i]
#     someText += str(someNumber)


def stringifyArray(arrayOfNumbers):
    newText = ""
    firstTime = True

    for number in arrayOfNumbers:
        if firstTime:
            firstTime = False
        else:
            newText += ", "
        newText += str(number)

    return newText

x = stringifyArray(someNumbers)
print(x)

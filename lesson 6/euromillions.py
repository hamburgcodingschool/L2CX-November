# CREATE A PROGRAM THAT RANDOMLY PICKS NUMBERS AND STARS FOR EURO MILLIONS

# numbers go from 1 to 50 (pick 5)
# stars go from 1 to 12 (pick 2)


import random

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

def generateNumberSequence(min, max, size):
    numbers = []

    for i in range(0, size):
        number = random.randint(min, max)
        while number in numbers:
            number = random.randint(min, max)
        numbers.append(number)

    numbers = sorted(numbers)
    return numbers


def generateEuroMillions():
    n = generateNumberSequence(1, 50, 5)
    s = generateNumberSequence(1, 12, 2)

    numbersText = stringifyArray(n)
    starsText = stringifyArray(s)

    # return "3, 12, 21, 34, 40 - 2, 5"

    return numbersText + " - " + starsText

print(generateEuroMillions())
print(generateEuroMillions())
print(generateEuroMillions())
print(generateEuroMillions())
print(generateEuroMillions())

# 6! = 6 * 5 * 4 * 3 * 2 * 1

number = 4 # ask for user input later
counter = 0
result = 1


while counter < number:
    counter = counter + 1
    result = result * counter


print("{}! = {}".format(number, result))
numbers = [23, 12, 34, 1, 3, 23, 11, 32]

checkNumber = 5

# # print True or False if number exists in array numbers
#
# foundIt = False
#
# for number in numbers:
#     if checkNumber == number:
#         foundIt = True
#         break
#
# if foundIt:
#     print("The number exists in the array!")
# else:
#     print("The number is not in the array!")

if checkNumber in numbers:
    print("The number exists in the array!")
else:
    print("The number is not in the array!")


# counter = 0
# while True:
#     print(counter)
#     counter = counter + 1
#     if counter == 10:
#         break




# ask user for secret PIN number (1234)
# if user enters the correct value, print "Welcome"
# if user enters the incorrect number, ask again
# if user fails 3 times, print ACCESS DENIED and end Program


# secretPIN = 1234
# userInput = 0000
#
# while userInput != secretPIN:
#     print("Please enter your PIN")
#     userInput = int(input())
#
# print("Welcome!")


secretPIN = 1234
userInput = 0000

counter = 0
canEnter = False

while counter < 3:
    counter = counter + 1
    print("Please enter your PIN")
    userInput = int(input())

    if secretPIN == userInput:
        canEnter = True
        break

if canEnter:
    print("Welcome!")
else:
    print("ACCESS DENIED")
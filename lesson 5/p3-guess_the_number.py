import random

secretNumber = random.randint(1, 100)

lives = 6

while lives > 0:
    print("What's your guess? You have {} tries left".format(lives))
    userNumber = int(input())

    if secretNumber > userNumber:
        print("You need to get higher...")
    elif secretNumber < userNumber:
        print("You need to get lower...")
    else:
        break

    lives -= 1

if lives > 0:
    print("YAY YOU WON!")
else:
    print("HA! HA! Smell you later")
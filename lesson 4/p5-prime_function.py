# def isPrime(number):
#     counter = 2
#     isPrime = True
#
#     while counter < number:
#         if number % counter == 0:
#             isPrime = False
#             break
#
#         counter = counter + 1
#
#     return isPrime


# function isPrime
def isPrime(number):
    counter = 2

    while counter < number:
        if number % counter == 0:
            return False

        counter = counter + 1

    return True

# main Code
print("Give me a number?")
inputNum = int(input())

if isPrime(inputNum):
    print("It's a prime")
else:
    print("It's not a prime")

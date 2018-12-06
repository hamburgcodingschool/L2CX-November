# function isPrime
def isPrime(number):
    counter = 2

    while counter < number:
        if number % counter == 0:
            return False

        counter = counter + 1

    return True



# main Code

# counter = 0
#
# while counter < 20:
#     counter = counter + 1
#     if isPrime(counter):
#         print(counter)

counter = 0
primesFound = 0

while primesFound < 100:
    counter = counter + 1
    if isPrime(counter):
        primesFound = primesFound + 1
        print("{}: {}".format(primesFound, counter))
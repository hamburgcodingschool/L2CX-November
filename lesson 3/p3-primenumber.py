number = 7 #ask user for input

counter = 2
isPrime = True

while counter < number:
    # print(counter)

    # print(number % counter)
    if number % counter == 0:
        isPrime = False
        break

    counter = counter + 1

if isPrime:
    print("YO IT IS A PRIME!")
else:
    print("NO PRIME HERE SUCKA!")
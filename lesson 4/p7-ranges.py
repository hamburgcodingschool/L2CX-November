
for i in range(1, 1000):
    if i % 9 == 0:
        print(str(i) + "!!!")
    elif i % 6 == 0:
        print(str(i) + "!!")
    elif i % 3 == 0:
        print(str(i) + "!")
    else:
        print(i)
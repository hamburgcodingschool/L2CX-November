# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

print("What's the number?")
number = int(input())

counter = 0

while counter < 10:
    counter = counter + 1
    res = number * counter
#     print(str(number) + " x " + str(counter) + " = " + str(res))
    print("{} x {} = {}".format(number, counter, res))

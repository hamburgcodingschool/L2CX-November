# times table
#
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# ...
# 7 x 10 = 70

print("Give me a number please")
number = int(input())

counter = 0
while counter < 10:
  counter = counter + 1
  res = number * counter
  # print( str(number) + " X " + str(counter) + " = " + str(res) )
  print("{} x {} = {}".format(number, counter, res))

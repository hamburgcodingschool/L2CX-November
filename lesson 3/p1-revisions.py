# print out all numbers from 1 to 1000
# add an ! to the numbers that are multiple of 5
# ex:
# ...
# 3
# 4
# 5!
# 6
# ...
# 29
# 30#
# ...

counter = 0

while counter < 100:
    counter = counter + 1

    # if counter % 10 == 0:
    #     print(str(counter) + "#")
    # else:
    #     if counter % 5 == 0:
    #         print(str(counter) + "!")
    #     else:
    #         print(counter)

    if counter % 10 == 0:
        print(str(counter) + "#")
    elif counter % 5 == 0:
        print(str(counter) + "!")
    elif counter % 3 == 0:
        print(str(counter) + "?")
    else:
        print(counter)
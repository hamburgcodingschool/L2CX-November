# decisions
#
# conditional operators
#
#   ==  !=  >  >=  <   <=

a = 200
b = 900
c = 200

if a > b:
  if a > c:
    print(a)
  else:
    print(c)
else:
  if b > c:
    print(b)
  else:
    print(c)

#another solution

if a > b:
  highest = a
else:
  highest = b

if c > highest:
  highest = c

print(highest)

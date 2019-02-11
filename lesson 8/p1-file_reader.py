
file = open('sample_data.csv', 'r')
next(file)

rows = file.readlines()


for row in rows:
    row = row.strip()
    newArray = row.split("r")
    print(newArray)
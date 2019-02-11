import csv

file = open('sample_data.csv', 'r')

data = csv.DictReader(file, delimiter=';')

for row in data:
    print(row['City'])
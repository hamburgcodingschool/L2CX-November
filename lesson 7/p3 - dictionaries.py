# DICTIONARIES
#

person1 = {
    "name": "Helder",
    "age": 37,
    "address": {
        "street": "Mein Strasse",
        "city": "HH",
        "country": "Germany"
    }
}

print(person1["name"])

# for key in person1:
#     print("{} => {}".format(key, person1[key]))

for key, value in person1.items():
    print("{} => {}".format(key, value))



# NAME, AGE, ADDRESS (STREET, CITY, COUNTRY)


print( person1["address"]["city"] )
# person = ["Quan", 40, "Single", 2, 11]
# person = {}
# print(person)


# person= {
#     "Name": "Quan"
#     "gender": "gay"
# }
# print(person)

person = {
    "name": "Quan",
    "age": "40",
}
for value in person.values():
    print(value)

# print(*person.keys())
for key, value in person.items():
    print(key, ":" ,value)
# update
# person["age"] = 22
# print(person)

#create
# person["home"] = "Ha Noi"
# print(person)

# del person["age"]
# print(person)

# # print(person)
# print(person["name"])
# person["age"] = 22
# print(person)

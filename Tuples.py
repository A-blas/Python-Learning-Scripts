
#Note: in tuples, the list cannot be edited or changed

coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])


phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

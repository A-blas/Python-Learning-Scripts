
from operator import truediv

price = 1000000

good_credit = True
bad_credit = False

if good_credit:
    print ("Put down 10% payment")

elif bad_credit:
    print ("Put down 20% payment")

print ("You must pay 100000 dollars for the house's down payment")



has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit: 
    print ("Eligible for loan")




temperature = int(input("What is the temperature outside? "))

if temperature >30:
    print("It's a hot day")

else: 
    print ("It's not a hot day")

name = ("Sandra")

if len(name) <3:
    print("Name must be at least 3 letters")

elif len(name) >50:
    print ("Name must be at most 50 letters")

else:
    print("Name looks good!")

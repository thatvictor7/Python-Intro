#Constant for tax and tip rate
TAX_RATE = 0.07
TIP_RATE = 0.15

#Get food charges into variable
food = input('Enter the charges for food. ')

#Calculate tip
tip = food * TIP_RATE

#Calculate tax
tax = food * TAX_RATE

#Calculate total 
total = food + tip + tax

#Print outputs
print(tip)
print(tax)
print(total)

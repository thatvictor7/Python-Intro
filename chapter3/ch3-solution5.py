#Chapter 3 solution 5
#Property Tax

#Main function calls request_value() function
def main():
    request_value()

#function displays message asking for value of property and user inputs amount
#gets saved to the value variable as a float. The calculate_assesed_value() 
#function is called with the value variable as an argument.
def request_value():
    value = float(input("Enter actual value of piece of property: "))
    calculate_assesed_value(value)

#function that takes an argument, it calculates the assesment value by 
#multiplying the actual_value argument by .60 which would be 60% and it's 
#saved to assesed_value variable. That variable is then printed and last, 
#calculate_property_tax() function with assesed_value as an argument.
def calculate_assesed_value(actual_value):
    assesed_value = actual_value * .60
    print("Tax will be assesed on a value of: $",assesed_value)
    calculate_property_tax(assesed_value)

#Function takes the assesed_value argument and calculates the tax
#amount by dividing by 100 and then multiplying by .64, it is saved to
#tax variable which is then
def calculate_property_tax(amount):
    tax = (amount / 100) * .64
    print("The property tax is: $", tax)

main()

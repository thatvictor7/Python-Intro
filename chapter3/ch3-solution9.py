#Chapter 3 solution 9
#Paint Job Estimator

#setting up for global variables of area to be painted, price of paint,
#gallons required for size of area, hours of labor and labor cost.
square_feet = 0
paint_price = 0
gallons_required = 0
hours = 0
labor_cost = 0

#main function calls all other functions
def main():
    request_square_feet()
    request_price_of_gallons()
    calculate_material(square_feet,paint_price)
    calculate_display_total_costs(gallons_required,labor_cost)

#function makes the square_feet variable into a global variable so it can be modified,
#then it displays message and gets input from user into square_feet varaible as a float.
def request_square_feet():
    global square_feet
    square_feet = float(input("Enter the number of square feet to paint. "))


#function makes the paint_price variable into a global variable displays message and 
# gets input from user into paint_price varaible as a float.
def request_price_of_gallons():
    global paint_price
    paint_price = float(input("Enter the price of a gallon of paint. "))

#function takes 2 arguments, square feet and gallons needed. Turns gallons_required,
# hours, and labor_cost into global variables. The square parameter is the square_foot amount
#requested previously, it is divided by 115 and will give you the gallons required and saved
#to gallons_required variable. It takes gallons_required times 8 to calculate hours and saves
# to hours global variable. Hours is multiplied by 20 and that determines cost of labor, saved 
#into labor_cost global variable.
def calculate_material(square,gallons):
    global gallons_required
    global hours
    global labor_cost
    gallons_required = square / 115 
    hours = gallons_required * 8
    labor_cost = hours * 20

#function takes 2 arguments, the gallon amount and labor cost total,
#it calculates total cost by multiplying gallons * paint price first and 
#adding labor cost. Then it prints all quantities and totals.
def calculate_display_total_costs(gallons,labor):
    total_cost = (gallons * paint_price) + labor
    print("Number of gallons", int(gallons))
    print("number of hours ", hours)
    print("Paint price: $%.2f" % paint_price)
    print("Labor: $%.2f" % labor)
    print("Total cost: $%.2f" % total_cost)

main()

'''
Victor Montoya
Chapter 10 Solution 8
Sales Report
21 July 2019
'''

def main():
    display_report()
    read_file()

def display_report():
    print("Brewster's Used Cars, Inc.\n")
    print("Sales Report")
    print("Salesperson ID \t\tSale Amount")
    print("===================================")

def read_file():
    total = 0
    sales_file = open("brewster.dat", "r")
    for sale in sales_file:
        # print(sale.split(','))
        salesperson = sale.split(",")[0]
        while salesperson == sale.split(",")[0]:
            total += float(sale.split(",")[1].strip("\n"))
            print(sale.split(",")[0], "\t", sale.split(",")[1])
            print(total)
            break
    # print(total)
        
        

main()
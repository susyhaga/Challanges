"""Create a Tip calculator (or rather a function for a tip calculator)!
    For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay. 
    Use variables to store the number of guests, the amount of the bill and the tip in percentage, e.g. 
           guest = 2
           bill = 80
           tipPercentage = 10
   Create a function which takes these values as input and outputs the total amount each guest needs to pay as well 
   as the amount of tip that is included, eg `Each guest needs to pay: 44 euro` and `The amount of tip for each guest is: 4 euro`."""
guest = 2
bill = 80
tipPercentage = 10
def calculator():
    percentage_x = bill * tipPercentage / 100
    print(percentage_x)
    tip_x = percentage_x / guest
    print(tip_x)
    bill_division = bill / guest
    print(bill_division)
    total = bill_division + tip_x
    print(total)
    return (total)
return_function = calculator()
print(f'Each guest needs to pay {return_function}')
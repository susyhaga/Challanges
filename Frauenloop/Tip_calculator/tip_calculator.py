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

    print(
        f'Each guest needs to pay {total} euros and The amount of tip for each guest is {tip_x}.')
    return (total)


calculator()

#Create a function that returns what type of week the day is (if it is a weekday or weekend day).
# Use get to simulate the switch method. 

def what_kind_week(day):
    days = {
        1: "Weekend",
        2: "Weekday",
        3: "Weekday",
        4: "Weekday",[]
        5: "Weekday",
        6: "Weekday",
        7: "Weekday",
        }
    return days.get(day, '**invalid**')

if __name__== "__main__":
    for day in range (0,9):
        print(f'{day}: {what_kind_week(day)}')

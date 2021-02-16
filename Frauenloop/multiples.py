#If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and you get 23.

#Find the sum of all the numbers between 1 and 1000 that are multiples of 3 or 5. 



__pdoc__ = {'main': False}


def sum_range_multiples_3_5(min, max):
    total = 0
    for i in range(min, max):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total


def main():
    x = 1
    y = 1000
    answer = sum_range_multiples_3_5(x, y)
    print(
        f"Sum of the numbers between {x} and {y} that are divisable by 3 or 5 is {answer}")
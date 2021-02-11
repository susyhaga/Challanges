__pdoc__ = {'main': False}


def sum_range_multiples_3_5(min, max):
    """ 
    Takes 2 paramaters and caluclates the total of the numbers between the paramaters that are divisable by 3 or 5. 

    Returns the total
    """
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


'''TEST'''

if __name__ == '__main__':
    main()


def test_totals():
    assert sum_range_multiples_3_5(1, 10) == 23
    assert sum_range_multiples_3_5(1, 100) == 2318
    assert sum_range_multiples_3_5(1, 1000) == 233168

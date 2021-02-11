"""If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and you get 23.

Find the sum of all the numbers between 1 and 1000 that are multiples of 3 or 5. 

Please upload your code and the output from your calculations """


sum = 0
for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        sum = sum+i
print(sum)

"""If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and you get 23.

Find the sum of all the numbers between 1 and 1000 that are multiples of 3 and 5. 

Please upload your code and the output from your calculations """
"""sum = 0
for i in range(1000):
    if(i % 3 == 0 and i % 5 == 0):
        sum = sum+i
print(sum)"""

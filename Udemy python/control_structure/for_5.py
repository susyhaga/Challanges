# Looping through a string

word = 'shenanigans'
for letter in word:
    print(letter)


word = 'shenanigans'
for letter in word:
    print(letter, end='')

# Looping through a list

approved = ['Eliza', 'Lucia', 'Italo', 'Mel']
for name in approved:
    print(f'{name} will be able to get less poor')

for position, name in  enumerate(approved):
    print (f'{position+1}', name)

#Lopping over a tuple

weekdays = ('Sunday', 'Monday', 'Tuesday', 
            'Wednesday', 'Thursday', ' Friday', 'Saturday')
for day in weekdays:
    print(f' Today is {day}')

#Lopping over a set

for letter in set('Cat are better than beer'):
    print(letter)

#Lopping over a literal set

for number in {1,2,3,4,5,6,7,8}:
    print(number)

#Lopping over a dictionary

product = {'name':'Bic', 'type':'pen', 'price':14.56, 'imported': True, 'id': 793}

for key in product:
    print(key)

for value in product.values():
    print(value)
    
for key,value in product.items():
    print(key,'=', value)
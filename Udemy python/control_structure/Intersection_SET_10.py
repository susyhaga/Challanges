#Create a constant with a set of forbidden words.
#Then create a list with some phrases. 
#Check if these prohibited words are inside the sentences and point out those words, 
#Otherwise the text will be authorized.


#Intersection set
FORBIDDEN_WORDS = {'asshole', 'bastard', 'Bolsonaro', 'hate', 'garlic'}
phrases = [
        "Bolsonaro is an asshole and bastard!",
        "Brazilian love beans with garlic and germans hate it",
        "Ramones is an amazing band",
]
for text in phrases:
    intersec = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersec:
        print("This phrase is forbidden:", intersec)
    else:
        print("This phrase is allowed:", text)


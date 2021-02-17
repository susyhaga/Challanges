#Create a constant with a tuple of forbidden words.
#Then create a list with some phrases. 
#Check if these prohibited words are inside the sentences. 
#Otherwise the text will be authorized.


#For WITHOUT else
FORBIDDEN_WORDS = ('asshole', 'bastard', 'Bolsonaro', 'hate', 'garlic')
phrases = [
        "Bolsonaro is a huge asshole. What a bastard!",
        "Brazilian love beans with garlic, but germans hate it",
        "Ramones is an amazing band",
]
for text in phrases:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print("This is a forbidden phrase:", word)
            found = True
            break

    if not found:
        print("This phrase is not dirty and imoral:", text)


#For WITH else
FORBIDDEN_WORDS = ('asshole', 'bastard', 'Bolsonaro', 'hate', 'garlic')
phrases = [
        "Bolsonaro is a huge asshole. What a bastard!",
        "Brazilian love beans with garlic, but germans hate it",
        "Ramones is an amazing band",
]
for text in phrases:
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print("This is a forbidden phrase:", word)
            break
        
        
    else:
        print("This phrase is not dirty and imoral:", text)


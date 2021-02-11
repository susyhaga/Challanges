# Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

# When positives and positives interact, they remain positive.
# When negatives and negatives interact, they remain negative.
# But when negatives and positives interact, they become neutral, and are shown as the number 0.The two strings will be the same length.

# neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.



def comparing_strings():
    result = ""
    word_1 = "--++-+--++"
    word_2 = "-+-++--++-"

    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            result = result+(word_1[i])
        else:
            result = result+("0")
    return result

end= comparing_strings()
print(end)




   

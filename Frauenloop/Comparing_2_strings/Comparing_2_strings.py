
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


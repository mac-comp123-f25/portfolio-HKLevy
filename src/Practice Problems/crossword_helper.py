def find_words(str):
    """Takes in a string with some blank spots represented by *.
    Returns all words acceptable in crosswords that follow that pattern."""
    word_file = open("../ica/TextFiles/crosswords.txt")
    word_length = len(str)
    word_list=[]
    for line in word_file:
        condition = True
        if len(line) == word_length+1: #+1 because there is the \n character
            for c in range(word_length):
                if str[c]!=line[c] and str[c]!='*':
                    condition = False
            if condition == True:
                word_list.append(line)
    return word_list

print(find_words('see****'))
print(find_words('e**o'))
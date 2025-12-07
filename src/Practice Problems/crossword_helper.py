def find_words_with(str,big_file):
    """Takes in a string, may include some blank spots represented by *.
    Returns all acceptable answers that have that string in any place inside them."""
    word_file = open(big_file)
    word_list=[]
    for line in word_file:
        if str in line:
            word_list.append(line)
    return word_list

def find_words_in_file(big_file,key):
    words=open(big_file)
    word_list=[]
    length=len(key)
    for line in words:
        #This will work by toggling the condition to false if something is wrong.
        #That way, if any part is false, condition=False. condition can never be switched back to True
        condition = True
        if len(line) == length+1:
            for letter in range(length):
                if key[letter]=='V' and line[letter] not in ['a','e','i','o','u','y']:
                    #If a vowel is requested and it's not a vowel (or y)...
                    condition = False
                elif key[letter]=='C' and line[letter] in ['a','e','i','o','u']:
                    #If a consonant is requested and it is a vowel (not y)...
                    condition = False
                elif key[letter]!='*' and key[letter]!='V' and key[letter]!='C' and key[letter]!=line[letter]:
                    #If it's a specific letter but it doesn't match...
                    condition = False

            if condition:
                #If every letter matched what we gave it...
                word_list.append(line)

    return word_list

def find_words(str):
    """Accepts *, C,V, or specific lowercase letters.
    Should consider acronyms and normal words. Add names later?"""
    word_list = find_words_in_file('better_crosswords.txt',str)
    word_list = word_list + find_words_in_file('crossword_acronyms_and_other.txt',str)
    word_list = word_list + find_words_in_file('crossword_names',str)

    word_list.sort()
    return word_list

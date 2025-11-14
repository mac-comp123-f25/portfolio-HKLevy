def i_words(file_path):
    file_in = open(file_path,'r')
    longstr = file_in.read()
    wordlist = longstr.split()
    file_in.close()
    return wordlist

print(i_words("../TextFiles/alice.txt"))
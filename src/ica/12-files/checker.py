def select_words(str,file_path):
    file_in = open(file_path,"r")
    my_list=[]
    for line in file_in:
        myline=line.strip()
        if str in myline:
            my_list.append(myline)
    return my_list, len(my_list)

wordlist, num = select_words('quo','../TextFiles/crosswords.txt')
# print(wordlist)
print(num)
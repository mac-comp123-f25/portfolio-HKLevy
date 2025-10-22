def select_words(str,file_path):
    file_in = open(file_path,"r")
    my_list=[]
    for line in file_in:
        if str in line:
            my_list.append(line)
    return my_list

print(select_words('abb','../TextFiles/shortcross.txt'))
def remove_all(value,my_list):
    while my_list.count(value)>0:
        my_list.remove(value)
    return my_list

print(remove_all(1,[3,1,4,1,5,9]))
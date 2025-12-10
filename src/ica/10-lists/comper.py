def times_n(number,list_of_nums):
    new_list = [number*x for x in list_of_nums]
    return new_list

def remove_all2(value,my_list):
    new_list = [x for x in my_list if x!=value]
    return new_list

print(times_n(3,[2,3,5,7,11,13,17,19]))
print(remove_all2(1,[3,1,4,1,5,9]))

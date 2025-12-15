def every_other(my_list):
    new_list=[]
    for index in range(len(my_list)):
        if index%2 == 0:
            new_list.append(my_list[index])
    return new_list

def sum_positive(my_list):
    sum = 0
    for item in my_list:
        if item > 0:
            sum = sum + item
    return sum


print(every_other([1,2,3,4,5,6,7,8,9]))
print(sum_positive([1,2,3,4,5,6,7,8,9]))
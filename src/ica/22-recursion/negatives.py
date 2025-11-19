def count_negatives(num_list):
    if len(num_list)==0:
        return 0
    else:
        first_num = num_list[0]
        if first_num < 0:
            return 1 + count_negatives(num_list[1:])
        else:
            return count_negatives(num_list[1:])

print(count_negatives([-2,3,5,-8,0]))
print(count_negatives([]))
print(count_negatives([-1,-2,-3,-4,-5]))
print(count_negatives([1,2,3,4,5,6,7,8,9]))
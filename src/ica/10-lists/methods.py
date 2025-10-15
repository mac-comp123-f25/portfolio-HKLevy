def end_points(list_of_nums):
    min_num = list_of_nums[0]
    max_num = list_of_nums[0]
    for item in list_of_nums:
        if item < min_num:
            min_num = item
        if item > max_num:
            max_num = item
    return (min_num, max_num)

test1 = end_points([3,1,4,1,5,9,2,6,5,3,5,8,0,2])
print(test1)

(min_num, max_num) = end_points([3,1,4,1,5,9,2,6,5,3,5,8,0,2])
print(min_num)
print(max_num)
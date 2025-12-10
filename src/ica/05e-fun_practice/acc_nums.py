def sum_range(start_val, end_val):
    count = 0
    for x in range(start_val, end_val+1):
        count = count+x
    return count

print(sum_range(1,4))
print(sum_range(3,3))
print(sum_range(5,1))
print(sum_range(-5,-6))
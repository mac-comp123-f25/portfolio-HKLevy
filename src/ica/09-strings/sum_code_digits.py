def sum_digits(list_words):
    total_sum = 0
    for word in list_words:
        digit_list=[]
        for char in word:
            if char.isdigit():
                digit_list.append(char)
        num_str = digit_list[0]+digit_list[-1]
        total_sum = total_sum + int(num_str)
    return total_sum

print(sum_digits(['jaw2n5btf9w', 'xxgg7x']))
print(sum_digits(['comp123', '1600grand', 'spring24']))

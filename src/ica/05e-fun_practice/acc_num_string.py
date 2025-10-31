def string_of_nums(num):
    acc = ''
    for x in range(num):
        acc = acc + ' ' + str(x+1)
    return acc
print(string_of_nums(10))
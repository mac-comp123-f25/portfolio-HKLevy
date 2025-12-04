def smallest_diff(x,y,z):
    print("Smallest_diff inputs:",x,y,z)
    diff1 = abs(x-y)
    diff2 = abs(y-z)
    diff3 = abs(x-z)
    min_diff = min(diff1, diff2, diff3)
    print("Differences:",diff1,diff2,diff3,", and Return Value:",min_diff)
    return min_diff

print(smallest_diff(3,5,9))
print(smallest_diff(32,43,90))
'''
Local environment:
x = 32
y = 43
z = 90

diff1 = abs(-11) = 11
diff2 = abs(-47) = 47
diff3 = abs(-58) = 58

min_diff = min(11,47,58) = 11
'''

def up_to_period(file_path):
    file_in = open(file_path,'r')
    long_str = file_in.read()
    new_str = ""
    for char in long_str:
        new_str = new_str + char
        if char == '.':
            break
    return new_str

print(up_to_period("../TextFiles/mockingbird.txt"))
def print_abbrev(file_path):
    file_in = open(file_path,'r')
    for line in file_in:
        line.strip()
        letters = line[0:20]
        print(letters)
    file_in.close()

print_abbrev("../TextFiles/alice.txt")
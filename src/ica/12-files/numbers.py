def write_to_n(int,file_path):
    outFile = open(file_path,"w")
    for i in range(1,int):
        outFile.write(str(i)+"\n")
    return outFile

print(write_to_n(19,"newname.txt"))
print(write_to_n(26,"newname.txt"))
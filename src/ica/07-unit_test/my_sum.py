def sum3(mylist):
    print(type(mylist))
    assert type(mylist) in [list,tuple]
    assert len(mylist)>=3
    for x in range(3):
        assert type(mylist[x]) in [int,float]

    return mylist[0]+mylist[1]+mylist[2]

if __name__ == "__main__":
  # print( sum3([5, 2, 8, -2, 6, 15]) )
  # print( sum3([5, 2]) )
  # print( sum3(5) )
  # print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )

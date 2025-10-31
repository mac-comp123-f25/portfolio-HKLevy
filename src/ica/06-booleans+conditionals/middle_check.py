def middle_value(n1,n2,n3):
    if n1>n2:
        if n2>n3:
            return n2
        elif n3>n1:
            return n1
        else:
            return n3
    elif n1>n3:
        if n2>n3:
            return n2
        elif n2<n3:
            return n3
        return n1
    else:
        if n2>n3:
            return n3
        else:
            return n2

if __name__ == "__main__":
  assert middle_value(5, 2, 77) == 5
  assert middle_value(-10, 50, 57) == 50
  assert middle_value(-1, -6, -3) == -3
  print("All tests passed!")

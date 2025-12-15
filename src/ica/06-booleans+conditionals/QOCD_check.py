def has_QOCD(string):
    if 'Q' in string or 'O' in string or 'C' in string or 'D' in string:
        return True
    else:
        return False

if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")

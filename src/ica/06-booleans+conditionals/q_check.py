def has_q(string):
    return 'q' in string

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")


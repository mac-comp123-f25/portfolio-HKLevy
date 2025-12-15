def percent_to_letter(grade):
    if grade>=90:
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    assert percent_to_letter(95) == "A"
    assert percent_to_letter(80) == "B"
    assert percent_to_letter(79) == "C"
    assert percent_to_letter(67) == "D"
    assert percent_to_letter(34) == "F"
    assert percent_to_letter(-52) == "F"
    print("All tests passed")
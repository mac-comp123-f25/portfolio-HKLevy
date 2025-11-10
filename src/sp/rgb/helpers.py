import tkinter as tk

def make_tk_color(r_val, g_val, b_val):
    """Takes in three color channel values: red, green, and blue, and
    makes a color string that tkinter can interpret correctly."""
    return "#%02x%02x%02x" % (r_val, g_val, b_val)


def get_num_from_entry(entry):
    """Takes in an Entry widget and extracts the string from it.
    It checks if it can convert the string to an integer, and if the
    resulting integer is between 0 and 255. If so, then it returns the
    integer. Otherwise, it returns 255 (if the string can't be converted or
    if its value is greater than 255), or 0 (if its value is negative)."""
    text = entry.get()
    text = text.strip()
    if text.isdigit() or (text[0] == "-" and text[1:].isdigit()):
        num = int(text)
    else:
        num = 255
        entry.delete(0, tk.END)
        entry.insert(0, "255")
    if num > 255:
        num = 255
        entry.delete(0, tk.END)
        entry.insert(0, "255")
    if num < 0:
        num = 0
        entry.delete(0, tk.END)
        entry.insert(0, "0")
    return num

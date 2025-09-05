"""
ICA on Sep. 5. Computes how many flowers will fit in a garden
when spaced 6 inches apart in precise rows adn columns.

@author Helen Levy (hlevy@macalester.edu
"""
bed_len = 30 #length in feet
bed_width = 3.5 #width in feet
num_of_columns = bed_len * 2
num_of_rows = bed_width * 2
total_flowers = num_of_columns * num_of_rows
print("A bed that is ", bed_len, " feet long and ", bed_width, "feet wide will fit ", total_flowers, "flowers.")

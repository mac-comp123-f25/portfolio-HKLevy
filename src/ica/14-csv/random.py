import csv

def read_csv(csv_filename):
    """
    Build a list of dictionaries from a CSV file without converting numeric
    values into integers.

    :param csv_filename: the name of the CSV file to read
    :return: list of field names (column headers in the CSV file) and
    list of dictionaries holding the data (one dictionary for each row)
    """
    data_in = open(csv_filename, 'r')
    csv_reader = csv.DictReader(data_in)
    fields = csv_reader.fieldnames

    table = []
    for rowDict in csv_reader:
        table.append(rowDict)
    data_in.close()
    return fields, table

field_names, sun_table = read_csv("DataFiles/sunRiseSet.csv")
print(field_names)
print(sun_table[0])  # printing just the first row of data
print_table(sun_table, field_names, 15)


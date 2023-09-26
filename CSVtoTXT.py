import csv

def quote_if_multiple_elements(item):
    # Check if the item contains more than one element (separated by spaces)
    if ' ' in item:
        return f'"{item}"'
    else:
        return item

with open('dataGladys2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    with open('data111.txt', 'w') as txt_file:
        for line in csv_reader:
            # Quote items if they contain multiple elements
            new_line = [quote_if_multiple_elements(item.replace(';', '\t')) for item in line]
            txt_file.write('\t'.join(new_line))
            txt_file.write('\n')

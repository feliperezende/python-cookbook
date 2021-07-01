import csv

with open('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            print('{} works in the {} department and is {} years old.'.format(row[0], row[1], row[2]))
        line_count += 1

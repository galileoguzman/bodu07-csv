import csv

file_name = 'workers.csv'
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{type(row)} - {row}')

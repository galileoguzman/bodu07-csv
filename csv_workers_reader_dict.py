import csv

file_name = 'workers.csv'
with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(f'{type(row)} - {row}')
        name = row.get('name')
        print(name)

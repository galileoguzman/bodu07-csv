import csv

file_name = 'workers.csv'
reader = csv.DictReader(open(file_name))
for row in reader:
    name = row.get('name')
    print(name)

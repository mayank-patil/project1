import csv

f = open('test.csv')
csv_f = csv.reader(f)

for row in csv_f:
    print(str(row))

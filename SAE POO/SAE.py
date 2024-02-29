import csv
with open('extraction-2021-2022-anonyme.csv', newline='', encoding='latin-1') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        for value in row:
            print(value)

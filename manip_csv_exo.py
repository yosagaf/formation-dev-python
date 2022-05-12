import csv
import argparse

parser = argparse.ArgumentParser(
    description="Exemple de manipulation de csv file.")
parser.add_argument("-f", "--file", dest="filename",
                    default="./data/departements.csv")

args = parser.parse_args()

# print(args.filename)
f = open(args.filename, "r")

fields = []
rows = []

with open(args.filename, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar=',')
    # Following command skips the first row of the CSV file.
    fields = next(data)
    for row in data:
        print(', '.join(row))

print("\nTotal no. of rows: %d" % (data.line_num))
print('Field names are:')
print(' , '.join(field for field in fields))

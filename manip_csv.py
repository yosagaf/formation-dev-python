import argparse
import csv
from ctypes import sizeof

parser = argparse.ArgumentParser(
    description="Exemple de manipulation de csv file.")
parser.add_argument("-f", "--file", dest="filename",
                    default="data/survey-financial.csv")

args = parser.parse_args()

# print(args.filename)
f = open(args.filename, "r")
reader = csv.reader(f)

print(dir(reader))

for row in reader:
    print(row)

f.close()

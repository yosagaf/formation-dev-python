import argparse
import sqlite3
import csv
import time

start_time = time.time()

parser = argparse.ArgumentParser(
    description="Importation de données.")

parser.add_argument("-c", "--csvfile", dest="csv_filename",
                    default="./data/departements.csv")

parser.add_argument("-d", "--dbfile", dest="database_filename",
                    default="./data/departements.db")
args = parser.parse_args()

conn = sqlite3.connect(args.database_filename)
c = conn.cursor()

# Création de la table Depts
c.executescript(""" DROP TABLE IF EXISTS Depts;
              CREATE TABLE Depts (department_id INTEGER, department_name VARCHAR(255), manager_id INTEGER, location_id TEXT);
            """)

with open(args.csv_filename, "r") as f:  # CSV file input
    # no header information with delimiter
    reader = csv.reader(f, delimiter=',')
    next(reader)

    for row in reader:
        # Appends data from CSV file representing and handling of text
        to_db = [row[0], row[1], row[2], row[3]]
        c.execute(
            "INSERT INTO Depts (department_id, department_name, manager_id, location_id) VALUES(?, ?, ?, ?);", to_db)

c.execute("""SELECT * FROM Depts""")

records = c.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")

for row in records:
    print("Department id: ", row[0])
    print("Departement name: ", row[1])
    print("Manager id: ", row[2])
    print("Location id: ", row[3])
    print("\n")

c.close()
conn.close()

print("--- %s seconds ---" % (time.time() - start_time))

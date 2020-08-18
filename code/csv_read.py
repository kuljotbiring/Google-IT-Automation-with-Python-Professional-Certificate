# this program assumes data in a file named csv_file.txt is formatted as follows:
# Sabrina Green, 802-867-5309, System Administrator
# Kuljot Biring, 516-782-3667, Cheif Information Officer

import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)

for row in csv_f:
    # unpack each row into variables and display them
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

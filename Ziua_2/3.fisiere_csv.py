import csv


with open("Ziua_2/3.fisier_csv.csv", "w") as fwriter:
    csv_writer = csv.DictWriter(fwriter, ["Ziua1", "Ziua2", "Ziua3"])
    for i in range(10):
        csv_writer.writerow({"Ziua1":"Luni", "Ziua2": "Marti", "Ziua3":"Miercuri"})



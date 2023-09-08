import csv

with open("weather.csv", "r") as fl:
    data = list(csv.reader(fl))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

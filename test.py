import csv

mileages = ['aaaa','bbbbb', 'ccccc']
prices = [1000,3232,2232]

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        mileages.append(float(row["km"]))
        prices.append(float(row["price"]))

print(mileages)
print(prices)
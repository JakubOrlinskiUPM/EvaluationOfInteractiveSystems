import csv
import random
import math


with open("./user_interactions.csv", "w") as file:
    writer = csv.writer(file)
    row = ["variant", "clickedYes"]
    writer.writerow(row)

    for i in range(1000):
        variant = round(random.random())
        if variant == 1:
            if math.floor(random.random() * 100) > 50:
                yes = 1
                no = 0
            else:
                yes = 0
                no = 1
        else:
            if math.floor(random.random() * 100) > 70:
                yes = 1
                no = 0
            else:
                yes = 0
                no = 1
        writer.writerow([variant, yes])







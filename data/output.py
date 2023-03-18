import csv
with open('daily_sales_data_0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['price'], row['date'], row['region'])

import csv
with open('daily_sales_data_1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['price'], row['date'], row['region'])

import csv
with open('daily_sales_data_2.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['price'], row['date'], row['region'])






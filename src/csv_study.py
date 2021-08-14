import csv

with open('src/data.csv', 'r') as f:

    reader = csv.reader(f)
    print(type(reader))
    for row in reader:
        print(row)

list_data = [
    ['a','b','c'],
    [1,2,3],
    [4,5,6]
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(list_data)


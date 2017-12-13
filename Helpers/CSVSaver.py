import csv

def listToCSV(lists ,path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in lists:
            writer.writerow(row)

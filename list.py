import csv
load_file = open("topCPU.txt.py", "r")
raw = load_file.readlines()
with open("topCPU.txt.py") as load_file:
    reader = csv.reader(load_file, delimiter=" ")
    data = [tuple(row) for row in reader]
load_file.close()
print (data)
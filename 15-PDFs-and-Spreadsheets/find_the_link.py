import csv

f = open("Exercise_Files/find_the_link.csv", encoding="utf-8")

csv_data = csv.reader(f)
data_lines = list(csv_data)
#print(len(data_lines))
#print(data_lines[0][0])

link = ""
idx = 0
for line in data_lines:
    link += line[idx]
    idx += 1

print("extracted link:")
print(link)

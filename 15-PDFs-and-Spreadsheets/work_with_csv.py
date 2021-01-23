import csv
import os

print(os.getcwd())

#open the file
data = open("example.csv", encoding='utf-8')

#csv.reader
csv_data = csv.reader(data)

#reformat it into a python object list of lists
data_lines = list(csv_data)

print(len(data_lines))

print("\n", data_lines[0])
print("\n", data_lines[0][1])

all_emails = []
for line in data_lines[1:5]:
    all_emails.append(line[3])

print(all_emails)


full_names = []
for line in data_lines[1:10]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names)
data.close()


file_to_output = open("to_save_file.csv", mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()

file_to_output = open("to_save_file.csv", mode='a', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['x', 'y', 'z'])
file_to_output.close()

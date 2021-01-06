import os
import csv


path = '/Users/anastasia/python_SGH/Our_data/'


try:
    if os.listdir(path) == []:
        raise FileNotFoundError
    for file in os.listdir(path):
        print(file)
        if file.endswith('.csv'):
            filepath = path + file
            if file.endswith('.csv'):
                file_copy = filepath[:-4] + "_copy.csv"

                with open(filepath, 'r') as csv_input:
                    with open(file_copy, 'w') as csv_output:
                        reader = csv.reader(csv_input)
                        writer = csv.writer(csv_output)
                        row0 = next(reader)
                        row0.append('% of change')
                        writer.writerow(row0)

                        for row in reader:
                            change = (float(row[4]) - float(row[1])) / float(row[1]) * 100
                            row.append(change)
                            writer.writerow(row)
                            print(row)


    for file in os.listdir(path):
        if file.endswith('.DS_Store'):
            raise FileNotFoundError


except FileNotFoundError:
    print("Folder is empty")
except UnicodeDecodeError:
    print("Can't read this file: " + str(file))
except PermissionError:
    print("Access to this file is denied: " + str(file))



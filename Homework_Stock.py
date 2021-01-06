import os
import csv
from pip._vendor.distlib.compat import raw_input

print('Enter a path to a folder which contains your csv files (without quotes) with a slash at the end:')
path = raw_input()


class NoCSVFile(Exception):
    pass

counter = 0
try:
    if not os.path.isdir(path):
        raise NotADirectoryError
    if os.listdir(path) == []:
        raise FileNotFoundError

    for file in os.listdir(path):

        try:
            if file.endswith('.csv'):
                counter += 1
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
        except ValueError:
            print("The file \"" + file + "\" has wrong or missing values!")

    if counter == 0:
        raise NoCSVFile

except FileNotFoundError:
    print("Folder is empty")
except NotADirectoryError:
    print("The specified path is not a directory or does not exist")
except NoCSVFile:
    print("There is no csv files in your folder.")

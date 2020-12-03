import os.path
import os
from pip._vendor.distlib.compat import raw_input


print('Enter a path to your folder here (without quotes):')
folder_path = raw_input()


def space_occupied(path):
    size = 0
    for i in os.scandir(path):
        if i.is_file():
            size += i.stat().st_size
        elif i.is_dir:
            size += space_occupied(i.path)
    return size


result = space_occupied(folder_path)
print('Space your folder occupies: ' + str(result) + ' bytes')


import os
import re


def rename_files():
    file_list = os.listdir("/Users/mayankgulaty/Downloads/prank")
    print(file_list)

    # error was coming in the for loop before changing directory that
    # system can't find the file
    os.chdir("/Users/mayankgulaty/Downloads/prank")

    for file_name in file_list:
        file_name_new = re.sub("\d+", "", file_name)
        os.rename(file_name, file_name_new)
        print(file_name, file_name_new)


rename_files()

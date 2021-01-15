import shutil
import os
import re


def first_step():
    zip_file = "unzip_me_for_instructions.zip"
    shutil.unpack_archive(zip_file, '', 'zip')


def browse_files_and_folders():

    print("\n")
    with open('extracted_content/Instructions.txt') as f:
        content = f.read()
        print(content)
    print("\n")

    crt_path = os.getcwd() + "\\extracted_content"

    for folder, subfolder, filenames in os.walk(crt_path):

        print("Current folder:", folder)

        for file in filenames:
            # print("Current File:", file)
            full_path = folder + "\\" + file

            # print("Search phone withing file:", full_path)
            search_file_for_phones(full_path)


def search_file_for_phones(file):

    # pattern = r"(\d{3})-(\d{3})-(\d{3})"
    pattern = r"\d{3}-\d{3}-\d{3}"

    my_file = open(file, 'r')
    result = re.findall(pattern, my_file.read())

    if len(result) > 0:
        print("\tPhone numbers found within the file:", file)
        print('\t\t', result)


if __name__ == "__main__":
    first_step()
    browse_files_and_folders()




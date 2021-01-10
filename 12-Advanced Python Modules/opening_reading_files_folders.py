import os
import shutil
import send2trash


def create_file():
    f = open('practice.txt', 'w')
    f.write("This is a test string")
    f.close()


def get_current_path():
    return os.getcwd()


def get_current_path_files():
    print(os.listdir())


def move_file():
    shutil.move('practice.txt', 'E:\\Workspace\\Complete-Python-3-Bootcamp')
    print("File practice.txt moved")


def delete_files():
    # delete file
    path = get_current_path()
    print("Current path: " + path)
    try:
        file = path + '\\practice.txt'
        # os.unlink(file)
        send2trash.send2trash(file)
    except:
        print('File : ' + file + " not found")

    # delete folder
    try:
        folder = path + "\\text"
        os.unlink(folder)
    except:
        print('Folder: ' + folder + " not found")


def walk_through_file_folder():
    path = get_current_path() + '\\Example_Top_Level'
    for folder, sub_folders, files in os.walk(path):

        print(f"\nCurrently looking at {folder}")
        print("\n")
        print("The subfolders are")

        for sub_fold in sub_folders:
            print(f"Subfolder : {sub_fold}")

        print("\n")
        print("The files are")

        for f in files:
            print(f"File : {f}")


if __name__ == "__main__":
    create_file()

    get_current_path()

    get_current_path_files()

    # move_file()

    delete_files()

    walk_through_file_folder()
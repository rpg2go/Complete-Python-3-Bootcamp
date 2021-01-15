import zipfile
import shutil

f = open("file_one.txt", "w+")
f.write("This is the first file")
f.close()


f = open("file_two.txt", "w+")
f.write("This is the second file")
f.close()

# compress files
comp_file = zipfile.ZipFile("files.zip", "w")
comp_file.write("file_one.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("file_two.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# decompress files
zip_obj = zipfile.ZipFile("files.zip", "r")
zip_obj.extractall("extracted_files")

# Creating a zip archive
zip_path = "E:\\Workspace\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules"
out_file = "example"
shutil.make_archive(out_file, 'zip', zip_path)

# Extracting a zip archive
shutil.unpack_archive("example.zip", "final_unzip", 'zip')
import shutil
import os 

source = input("Enter source file with full path: ")
destination_path = input("Enter destination file with full path: ")

shutil.copyfile(source,destination_path)

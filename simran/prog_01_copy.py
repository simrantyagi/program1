import os 
print("Current working directory: {0}".format(os.getcwd()))



import shutil

file = r'/home/simran.tyagi/Downloads/conda_dr/simran/file1.txt' ## enter the path of the original file with file name and extension
copied_file = r'/home/simran.tyagi/Downloads/conda_dr/simran2/copyfile.txt' ## enter the path where you want to copy your file with the filename you want to give and extension

shutil.copyfile(file,copied_file)
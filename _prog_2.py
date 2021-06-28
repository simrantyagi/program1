
import shutil
import os
src_dir = 'fol1'
dest_dir = 'fol2'

files = os.listdir(src_dir)
shutil.copytree(src_dir, dest_dir)

import os
import pathlib
import argparse
import shutil
from os.path import join, splitext
from glob import glob
from collections import Counter
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy directory")
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    file = pathlib.Path(args.source)
    if file.exists():
        shutil.copytree(args.source, args.destination, dirs_exist_ok=True)
    else:
        print("Directory not exist")
    print("The source_dest is: ", args.source)

    totalFiles = 0
    for base, dirs, files in os.walk(args.destination):
        print('The destination where files are copying: ', base)
        for Files in files:
            totalFiles += 1
        print(f"Total number of files copied = {totalFiles}")


    path = args.destination
    c = Counter([splitext(i)[1][1:] for i in glob(join(path, '*'))])
    for ext, count in c.most_common():
        print(ext, count)

    for i in tqdm(range(100)):
        ...









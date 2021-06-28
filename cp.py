import pathlib
import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy directory")
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    file = pathlib.Path(args.source)
    if file.exists():
        shutil.copytree(args.source, args.destination, dirs_exist_ok=True)
    else:
        print(" Directory not exist")










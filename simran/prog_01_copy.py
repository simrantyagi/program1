import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Copy file")
    parser.add_argument('source',type=argparse.FileType('r'))
    parser.add_argument('destination', type=argparse.FileType('w'))
    args = parser.parse_args()
    print(args.source)

shutil.copyfile(args.source, args.destination)

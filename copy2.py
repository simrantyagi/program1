import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Copy directory")
    parser.add_argument('source',type=argparse.FileType('r'))
    parser.add_argument('destination', type=argparse.FileType('w'))
    args = parser.parse_args()
    shutil.copytree(args.source,args.destination)



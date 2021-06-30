from tqdm import tqdm
import time
import argparse
import shutil
import os
import split
media_type = {'Media_File':0, 'Text_File':0, 'Other':0}
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Copy file")
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    folder_path = args.source
    _path = os.listdir(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for f in tqdm(files):
            print("Copying file from src to destination")
            if not os.path.exists(args.destination):
                os.mkdir(args.destination)
            for item in os.listdir(folder_path):
                file_path = os.path.join(args.source, item)
                if os.path.isfile(file_path):
                    shutil.copy(file_path, args.destination)
            time.sleep(2)
            print(root, f)

    if _path.split('.')[-1] == '.png, .mp4, .mp3, .jpg, .jpeg':

        media_type[media_file] +=1
    elif _path.split('.')[-1] == ' .txt, .doc, .docx, .rtf':
        media_type['Text_File']+=1
    else:
        media_type['other'] += 1

    print(f"Copy report {media_type}")









    

        












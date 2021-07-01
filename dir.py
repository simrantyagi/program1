from tqdm import tqdm
import time
import argparse
import shutil
import os
import split
from pathlib import Path
import mimetypes
media_type = {'media_file': 0, 'text_file': 0, 'other': 0}
file_count=0
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= "Copy file")
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    folder_path = args.source
    _path =os.listdir(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for f in tqdm(files):
                print("Copying file from src to destination")
                if not os.path.exists(args.destination):
                    os.mkdir(args.destination)
                for item in os.listdir(folder_path):
                    file_path = os.path.join(args.source, item)
                    if os.path.isfile(file_path):
                        shutil.copy(file_path, args.destination)
                else:
                        for _, _, dest in os.walk(args.destination):
                            for _sfile in dest:
                                if os.path.isfile(_sfile):
                                    file_count += 1
                time.sleep(2)
                print(root, f)
            for sfile in files:
                file_extension = os.path.splitext(sfile)[-1]
                if file_extension in '.png, .mp4, .mp3, .jpg,.jpeg':
                    media_type['media_file']= media_type.get('media_file')+ 1
                elif file_extension in  ' .txt, .doc, .docx, .rtf':
                    media_type['text_file'] = media_type.get('text_file') + 1
                else:
                    media_type['other'] = media_type.get('other') + 1
    print(media_type)
    print(file_count)














        






























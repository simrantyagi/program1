import pathlib
import argparse
import shutil
from future.moves import tkinter as Tk
from tkinter import *
from tkinter import messagebox
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy directory")
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    file = pathlib.Path(args.source)
    if file.exists():
        shutil.copytree(args.source, args.destination, dirs_exist_ok=True)
    else:
        top = Tk()
        top.geometry("100x100")
        messagebox.showerror("error","Source Directory not exists")










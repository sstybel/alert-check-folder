import os
import sys
import argparse
from tkinter import Tk, messagebox

str_version = "1.00"
str_app_name ="Alert Check Folder - ver. " + str_version
str_author = "Copyright (c) 2025 by Sebastian Stybel, www.BONO.Edu.PL"
      
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--folder", help="Path to the folder to check existence", default=r"C:\\audyt")
parser.add_argument("--message-title", help="Title of the message box", default="Audit !!!")
parser.add_argument("--message-text", help="Text of the message box", default="Folder found: C:\\audyt")
parser.add_argument("--message-icon", help="Icon of the message box (info, warning, error)", default="error")
parser.add_argument("-h", "--help", help="Show this help message and exit", action="store_true")
args = parser.parse_args()

def check_folder(folder_path, title, text, icon):  
    if args.help:
        parser.print_help()
    else:
        text_show = text + "\n\n" + str_app_name + "\n" + str_author
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            root = Tk()
            root.withdraw()
            
            messagebox.showinfo(title, text_show, icon=icon)
            root.destroy()

if __name__ == "__main__":
    check_folder(args.folder, args.message_title, args.message_text, args.message_icon)

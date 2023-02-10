

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import datetime
import shutil


import file_transfer_main.py






#Creates function to select source directory.
def SourceDir(self):
    selectSourceDir = tkinter.filedialog.askdirectory()
    #The .delete(0, END) will clear the content that is the Entry widget,
    #this allows the path to be inserted into the Entry widget properly.
    self.source_dir.delete(0, END)
    #The .insort mothod will insert the user selection to the source_dir Entry
    self.source_dir.insert(0, selectSourceDir)

            

#Creates function to select destination directory.
def destDir(self):
    selectDestDir = tkinter.filedialog.askdirectory()
    #The .delete(0, END) will clear the content that is inserted in the Entry widget,
    #this allows the path to be inserted into the Entry widget properly.
    self.destination_dir.delete(0, END)
    #The .insert method will insert the user selection to the destination_dir Entry widget
    self.destination_dir.insert(0, selectDestDir)

            
#Creates function to transfer files from on directory to another
def transferFiles(self):
    #Path to the file
    path = (r"C:\Users\Esia Adam\Documents\GitHub\Python Projects\Customer Source\file1.txt",
            "C:\Users\Esia Adam\Documents\GitHub\Python Projects\Customer Source\file2.txt",
            "C:\Users\Esia Adam\Documents\GitHub\Python Projects\Customer Source\file3.txt")

    def is_file_older_than_x_days(path, days=1):
        #File modification timestamp of a file
        file_time = path.getmtime(path) 
        # Check against 24 hours 
        return ((time.time() - file_time) / 3600 > 24*days)
    
    #Gets source directory
    source = self.source_dir.get()
    #Gets destination directory
    destination = self.destination_dir.get()
    #Gets a list of files in the source dierctory
    source_files = os.listdir(source)
    #Runs through each file in the source directory
    for i in source_files:
        #moves each file from the source to the destination
        shutil.move(source + '/' + i, destination)
        print(i + ' was successfully transferred.')

#Creates function to exit program
def exit_program(self):
    #root is the main GUI widow, the Tkinter destroy method
    #tells python to terminate root.mainloop and all widgets inside the GUI window
    root.destroy()


if __name__ == "__main__":
    pass

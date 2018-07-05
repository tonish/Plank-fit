import Tkinter as Tk
from tkFileDialog import askopenfilename
import os

def get_file(ftype, message):
    root = Tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(filetypes = (ftype) , title = message) # show an "Open" dialog box and return the path to the selected file
    return filename

# a = get_file([('python file', '*.py'), ('all formats', '.*')], 'hello')
# b = os.path.split(a)
# print b[1][:-3]
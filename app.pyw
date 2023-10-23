import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askdirectory
#from tkinter.messagebox import showinfo
import sqlParser as sqlp

def output_to_json():
    path = askdirectory()
    path += "\output.json"
    open(path, 'a').close()
    with open(path, "w+") as outfile:
        outfile.write(script.to_json())

def parse():
    global script
    global isParsed

    script = sqlp.Script(filename)
    isParsed = True
    changeBtnState("outputJsonBtn")

def select_file():
    global fileIsSelected
    global filename

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    fileIsSelected = True
    changeBtnState("parseBtn")

def changeBtnState(btn):
    global parseBtn
    global outputJsonBtn
    global fileIsSelected

    if btn == "parseBtn" and fileIsSelected:
        parseBtn.config(state=NORMAL)
    elif btn == "parseBtn":
        parseBtn.config(state=DISABLED)
        
    
    if btn == "outputJsonBtn" and isParsed:
        outputJsonBtn.config(state=NORMAL)
    elif btn == "outputJsonBtn":
        outputJsonBtn.config(state=DISABLED)

def Main():
    global parseBtn
    global outputJsonBtn

    window = Tk()
    window.title("SQLParser+ - Dolotboy")
    window.grid()
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    frm = ttk.Frame(window, padding=10)
    frm.grid()
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_columnconfigure(0, weight=1)

    ttk.Label(frm, text="SQLParser+ - V.0.6.1").grid(column=0, row=0)

    selectScriptBtn = ttk.Button(frm, text="Select script", command=select_file)
    selectScriptBtn.grid(column=0, row=1)

    parseBtn = ttk.Button(frm, text="Parse", command=parse)
    parseBtn.grid(column=0, row=2)
    parseBtn.config(state=DISABLED)

    outputJsonBtn = ttk.Button(frm, text="Output JSON", command=output_to_json)
    outputJsonBtn.grid(column=0, row=3)
    outputJsonBtn.config(state=DISABLED)

    window.mainloop()

if __name__ == "__main__":
    parseBtn = None
    outputJsonBtn = None
    fileIsSelected = False
    isParsed = False
    filename = None
    script = None
    
    Main()
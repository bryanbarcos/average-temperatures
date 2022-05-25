from ctypes.wintypes import WORD
import tkinter as tk

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=35, text=field+': ', anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, '')
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

def display_result(root, result_list, result_total):
    '''
    Add a textbox with the results to the GUI
    '''
    t = tk.Text(root, height=5, width=50)

    for x in result_list:
        t.insert(tk.END, x + '\n')
    t.insert(tk.END, result_total + '\n')
    t.pack()

def display_help(root):
    '''
    Display an explanation and example of cities input format
    '''

    tutorial = ("You can get your API key by signing up for free at https://www.visualcrossing.com/sign-up\n\n" +
                "FROM date and TO date are inclusive.\n\n" +
                "Cities are separated by a '-'. Include the country, state, or province for higher accuracy.\n\n" +
                "Example input: FROM: 2022-05-01    TO: 2022-05-10   CITIES: Toronto,Ontario - Barcelona,Spain")

    tutorial_window = tk.Tk()
    tutorial_window.title('Help')
    t = tk.Text(tutorial_window, height=7, width=100)
    t.insert(tk.END, tutorial)
    t.pack()
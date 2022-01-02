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
import tkinter as tk

def final_balance(entries):
    # period rate:
    print("FINAL_BALANCE_FUNCTION_CALL")
    print(entries['From [YYYY-MM-DD]'].get())
    print(entries['To [YYYY-MM-DD]'].get())
    print(entries['Cities'].get())

    locations = entries['Cities'].get()
    cities = locations.split(" - ")
    print(cities)
    print(cities[0])

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "")
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
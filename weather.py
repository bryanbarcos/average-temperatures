import tkinter as tk

fields = ('API KEY', 'From [YYYY-MM-DD]', 'To [YYYY-MM-DD]', 'Cities')

if __name__ == '__main__':
    import weather_gui as wg

    root = tk.Tk()
    ents = wg.makeform(root, fields)
    b1 = tk.Button(root, text='Get Average Temp',
           command=(lambda e=ents: wg.final_balance(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
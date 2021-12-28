import tkinter as tk

fields = ('API KEY', 'From [YYYY-MM-DD]', 'To [YYYY-MM-DD]', 'Cities')
baseUrl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/'

cities_list = []
from_date = ''
to_date = ''
api_key = ''

def process_entries(entries):

    # Remove whitespaces in case for mistake during user input
    locations = entries['Cities'].get()
    locations2 = locations.replace(' ', '')
    cities_list = locations2.split('-')

    from_date = entries['From [YYYY-MM-DD]'].get()
    to_date = entries['To [YYYY-MM-DD]'].get()
    api_key = entries['API KEY'].get()

if __name__ == '__main__':
    import weather_gui as wg

    root = tk.Tk()
    ents = wg.makeform(root, fields)
    b1 = tk.Button(root, text='Get Average Temp',
           command=(lambda e=ents: process_entries(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
import tkinter as tk
import csv
import codecs

fields = ('API KEY', 'From [YYYY-MM-DD]', 'To [YYYY-MM-DD]', 'Cities', 'Calculated Average Temperature')
baseUrl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
unitGroup = 'metric'
contentType = 'csv'

cities_list = []
from_date = ''
to_date = ''
api_key = ''


def make_url(location):
    '''
    Creates the url for the api call
    '''
    url = baseUrl + location + '/' + from_date + '/' + to_date + '?'

    url+='&unitGroup=' + unitGroup

    url+='&include=obs,days'

    url+='&elements=temp'

    url+='&key=' + api_key

    return url

def process_entries(entries):
    '''
    Process user input and place values into global variables 
    for further processing
    '''

    # Remove whitespaces in case for mistake during user input
    locations = entries['Cities'].get()
    locations2 = locations.replace(' ', '')
    cities_list = locations2.split('-')

    from_date = entries['From [YYYY-MM-DD]'].get()
    to_date = entries['To [YYYY-MM-DD]'].get()
    api_key = entries['API KEY'].get()

def read_csv(csv_bytes):
    csv_text = csv.reader(codecs.iterdecode(csv_bytes, 'utf-8'))

    row_index = 0

    for row in csv_text:
        if row_index == 0:
            first_row = row

        else:
            print('Weather in ', row[0], ' on ', row[1])

            col_index = 0
            for col in row:
                if col_index >= 4:
                    print('  ', first_row[col_index], ' = ', row[col_index])
                col_index += 1
        row_index += 1

    # If there are no CSV rows then something fundamental went wrong
    if row_index == 0:
        print('Sorry, but it appears that there was an error connecting to the weather server.')
        print('Please check your network connection and try again..')

    # If there is only one CSV  row then we likely got an error from the server
    if row_index == 1:
        print('Sorry, but it appears that there was an error retrieving the weather data.')
        print('Error: ', first_row)

def calculate_average(entries):
    process_entries(entries)

    

if __name__ == '__main__':
    import weather_gui as wg

    root = tk.Tk()
    ents = wg.makeform(root, fields)
    b1 = tk.Button(root, text='Get Average Temp',
           command=(lambda e=ents: calculate_average(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
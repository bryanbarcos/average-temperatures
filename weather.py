import tkinter as tk
import csv
import codecs
from urllib import response
import urllib.request
import urllib.error
import sys
import json

fields = ('API KEY', 'From [YYYY-MM-DD]', 'To [YYYY-MM-DD]', 'Cities', 'Calculated Average Temperature')
baseUrl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
unitGroup = 'metric'

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

    global cities_list
    global from_date
    global to_date
    global api_key

    # Remove whitespaces in case for mistake during user input
    locations = entries['Cities'].get()
    locations2 = locations.replace(' ', '')
    cities_list = locations2.split('-')

    from_date = entries['From [YYYY-MM-DD]'].get()
    to_date = entries['To [YYYY-MM-DD]'].get()
    api_key = entries['API KEY'].get()

def calculate_average(entries):
    process_entries(entries)

    for loc in cities_list:
        api_call = make_url(loc)
        
        try:
            csv_bytes = urllib.request.urlopen(api_call)
        except urllib.error.HTTPError as e:
            error_info = e.read().decode()
            print('Error code: ', e.code, error_info)
            sys.exit()

        except urllib.error.URLError as e:
            error_info = e.read().decode()
            print('Error code: ', e.code, error_info)
            sys.exit()

        string = csv_bytes.read().decode('utf-8')
        response = json.loads(string)

        # TESTING PURPOSES
        print(response['days']) 

        days_temp_response = []

        # move response dict elements into list
        for x in response['days']:
            days_temp_response.append(x['temp'])
        print(days_temp_response)
        avg = sum(days_temp_response) / len(days_temp_response)
        print(loc + ' avg = ' + str(avg))

if __name__ == '__main__':
    import weather_gui as wg

    root = tk.Tk()
    root.title('Average Weather')
    ents = wg.makeform(root, fields)
    b1 = tk.Button(root, text='Get Average Temp',
           command=(lambda e=ents: calculate_average(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
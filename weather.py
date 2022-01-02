import tkinter as tk
from urllib import response
import urllib.request
import urllib.error
import sys
import json
import weather_gui as wg

fields = ('API KEY', 'From [YYYY-MM-DD]', 'To [YYYY-MM-DD]', 'Cities')
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

    # Get all values from the user input in the GUI
    # Remove whitespaces in case for mistake during user input
    locations = entries['Cities'].get()
    locations2 = locations.replace(' ', '')
    cities_list = locations2.split('-')

    from_date = entries['From [YYYY-MM-DD]'].get()
    to_date = entries['To [YYYY-MM-DD]'].get()
    api_key = entries['API KEY'].get()

def calculate_average(entries, root):

    process_entries(entries)

    total_avg = 0
    final_result = []
    total_avg_result = ''

    for loc in cities_list:
        api_call = make_url(loc)
        
        # make the api call to visual crossing server
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

        # reads the response from the server and stores the JSON obj
        string = csv_bytes.read().decode('utf-8')
        response = json.loads(string)

        days_temp_response = []

        # move response dict elements into list
        for x in response['days']:
            days_temp_response.append(x['temp'])

        # calculate average temp for the current location object
        avg = sum(days_temp_response) / len(days_temp_response)
        total_avg += avg
        avg = round(avg, 2)
        city_result = loc + ' Average Temp = ' + str(avg)
        final_result.append(city_result)

    # calculate average temp of all locations
    total_avg = total_avg / len(cities_list)
    total_avg = round(total_avg, 2)
    total_avg_result = 'Total Average = ' + str(total_avg)

    wg.display_result(root, final_result, total_avg_result)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Average Weather')

    # calls the makeform function inside the file weather_gui.py 
    ents = wg.makeform(root, fields)

    # Create the buttons that will be on the GUI
    b1 = tk.Button(root, text='Get Average Temp',
        command=(lambda e=ents: calculate_average(e, root)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
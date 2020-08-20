import requests
import ciso8601
import datetime

'''
Makes the api call to launch library.

args:
    None

return:
    api call return as a json object
'''
def launch_init():
    URL = 'https://ll.thespacedevs.com/2.0.0/launch/upcoming/?mode=detailed'
    r = requests.get(url = URL)
    data = r.json()
    results = data['results']
    for result in results:
        net = datetime.datetime.strptime(result['net'], '%Y-%m-%dT%H:%M:%SZ')
        if (net > datetime.datetime.utcnow()):
            return result
            
    
'''
Returns the launch information url. If there is no information, None is returned.

args:
    data - the JSON data from the api call.

return:
    None - If the length of the array is zero, it can be assumed there is no information for this launch
    data_array[0] - The first entry in the array is the primary data source for this metric
'''
def get_launch_info_url(data):
    data_array = data['launches'][0]['infoURLs']
    if len(data_array) == 0:
        return None
    return data_array[0]

'''
Returns the video stream url. If there is no information, None is returned.

args:
    data - the JSON data from the api call.

return:
    None - If the length of the array is zero, it can be assumed there is no stream for this launch
    data_array[0] - The first entry in the array is the primary data source for this metric
'''
def get_stream_url(data):
    data_array = data['vidURLs']
    if len(data_array) == 0:
        return None
    return data_array[0]
'''
Returns a formatted string that is used by the countdown script.

args:
    date_string - the time and date information in the form of a string

return:
    Re-formatted string of the date_string.
'''
def get_timedate_stamp(date_string):
    dt = ciso8601.parse_datetime(date_string)
    dt_st = ('%s, %s, %s, %s, %s, %s'% (dt.year, (dt.month-1), dt.day, dt.hour, dt.minute, dt.second))
    return dt_st
'''
Takes a date string from the API and returns a re-formatted string that is easier to read for the UI.

args:
    date_string - the time and date information in the form of a string

return:
    A reformatted date string.
'''
def datetime_to_string(date_string):
    dt = ciso8601.parse_datetime(date_string)
    return dt.strftime("%B %d, %Y | %H:%M:%S UTC")

'''
Takes the img url from the api as an argument and returns our own default image if the placeholder from the api is used. Otherwise, use the passed url.

args:
    api_string - the url string from the api

return:
    string - custom placeholder or the appropriate img url
'''
def get_img_url(api_string):
    if ('placeholder' in api_string):
        return 'https://i.imgur.com/YT5cdel.png'
    api_string = api_string.replace('\\', '')
    return api_string




class Launch:
    def __init__(self):
        data = launch_init()
        self.mission = data['name']
        try:
            self.mission_description = data['mission']['description']
        except TypeError:
            self.mission_description = None
        self.launch_complex = data['pad']['location']['name']
        self.launch_complex_info_url = data['pad']['wiki_url']
        self.lsp = data['launch_service_provider']['name']
        self.lsp_country = data['pad']['location']['country_code']
        self.rocket_name = data['rocket']['configuration']['name']
        self.rocket_info_url = data['rocket']['configuration']['wiki_url']
        self.net = get_timedate_stamp(data['net']) #UTC
        self.img_url = get_img_url(data['image'])
        self.launch_time_date = datetime_to_string(data['net'])
        self.lsp_abbrev = data['launch_service_provider']['abbrev']
        self.lsp_info_url = data['launch_service_provider']['wiki_url']
        self.stream = get_stream_url(data)
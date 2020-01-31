import requests
import ciso8601

'''
Makes the api call to launch library.

args:
    None

return:
    api call return as a json object
'''
def launch_init():
    URL = 'https://launchlibrary.net/1.4/launch/next/1'
    r = requests.get(url = URL)
    return r.json()

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

TODO: Refactor with other array functions
'''
def get_stream_url(data):
    data_array = data['launches'][0]['vidURLs']
    if len(data_array) == 0:
        return None
    return data_array[0]
'''
Returns a datetime object given a string. The string in the api call matches what is needed for this conversion to work properly, out of the box.

args:
    date_string - the time and date information in the form of a string

return:
    date - a datetime object of the previously passed string
'''
def get_timedate_stamp(date_string):
    dt = ciso8601.parse_datetime(date_string)
    dt_st = ('%s, %s, %s, %s, %s, %s'% (dt.year, (dt.month-1), dt.day, dt.hour, dt.minute, dt.second))
    return dt_st

'''
Takes the img url from the api as an argument and returns our own default image if the placeholder from the api is used. Otherwise, use the passed url.

args:
    api_string - the url string from the api

return:
    custom placeholder or the appropriate img url
'''
def get_img_url(api_string):
    if ('placeholder' in api_string):
        return 'https://i.imgur.com/tMGPxej.png'
    api_string = api_string.replace('\\', '')
    return api_string

class Launch:
    def __init__(self):
        data = launch_init()
        self.name = data['launches'][0]['name']
        self.lsp = data['launches'][0]['lsp']['name']
        self.info = get_launch_info_url(data)
        self.rocket_name = data['launches'][0]['rocket']
        self.stream = get_stream_url(data)
        self.net = get_timedate_stamp(data['launches'][0]['isonet']) #UTC
        self.img_url = get_img_url(data['launches'][0]['rocket']['imageURL'])


# sandbox
l = Launch()
print(l.net)





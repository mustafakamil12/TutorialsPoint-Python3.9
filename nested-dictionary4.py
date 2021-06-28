import requests
import xml
import xml.etree.ElementTree as ET

agent = {'env_proxy':1, 'keep_alive':1, 'timeout':30}

call = 'http://api.weatheranalytics.com/v2/wsi/metar/[39.45,-74.5667]?startDate=06/22/2021&endDate=06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'


def ParseWXA_XML(site_id,data_response):
    print("----Function ParseWXA_XML start----")
    # XMLin returns a hash_ref
    # Parse XML with ElementTree
    weather_records = []
    tree = ET.fromstring(data_response.content.decode("utf-8"))
    #tree = data_response.decode("utf-8")
    print(tree)
    root = tree
    if root.iter('Hour'):
        for hour in root.iter('Hour'):
            weather_records.append(hour)

        print("weather_records = ", weather_records)

        for elem in weather_records:
            dateHrGmt = elem.getchildren()
            print("dateHrGmt = ", dateHrGmt)
            for record in dateHrGmt:
                print("record = ", record)
                record_hash = record
                valid_time = ParseFormattedDateTime(record_hash.text)
                #print("valid_time = ", valid_time)
                #print("record_hash.text => ",record_hash.text)
        #print("weather_records = ", weather_records)

def ParseFormattedDateTime(date_str):

    #OLD: 10/17/2015 5:00:00 AM ->  2015-10-17T05:00:00Z

    #NEW1: 2015-10-17 05:00:00.0 ->  2015-10-17T05:00:00Z
    #NEW2: 10/20/2015 05:00:00

    # check if the input is in the format of "2015-10-17 05:00:00.0"

    print("Input => date_str = ", date_str)
    if date_str.find("-") != -1 :
        date_str
        date_str = re.sub(r'.(\d+)$','Z',date_str)
        date_str = re.sub('(\s)','T',date_str)
        return date_str

    #otherwise, the format is "10/20/2015 05:00:00"
    print("date_str = ", date_str)
    time_parts = date_str.split(" ")
    print("time_parts = ", time_parts)
    date = ""
    time = time_parts[1]

    date_parts = []
    date_parts = time_parts[0].split("/")

    mm = date_parts[0].strftime("%02d")
    dd = date_parts[1].strftime("%02d")
    yyyy = date_parts[2]

    return f"{yyyy}-{mm}-{dd}T{time}Z"


response = requests.get(call,params=agent)
site = 17045
ParseWXA_XML(site, response)

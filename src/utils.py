import datetime
import json
import requests
from dicttoxml import dicttoxml

URL = "https://my-json-server.typicode.com/dim4iksh/test/db"

def convert_to_xml():
    files = get_data('files')
    xml = dicttoxml(files)
    print(xml.decode('utf-8'))
    return xml

def oldest_item():
    files = get_data('files')
    oldest_file = None
    for file in files:
        if not oldest_file or datetime.datetime.strptime(oldest_file['date'],
                                                         "%d.%m.%y") > datetime.datetime.strptime(file['date'],
                                                                                                  "%d.%m.%y"):
            oldest_file = file
    return json.dumps(oldest_file, indent=4)

def print_info():
    files = get_data('files')
    dict_info = {}
    for file in files:
        if not file['file_type'] in dict_info:
            dict_info[file['file_type']] = 1
        else:
            dict_info[file['file_type']] = dict_info[file['file_type']] + 1
    return f"number of each filetype in the db: \n{str(dict_info)}"

def save_file():
    data = get_data()
    ts = datetime.datetime.now().strftime("%d-%m-%Y%H_%M_%S")
    file_name = f"data_{ts}.json"
    with open(file_name, "w") as f:
        f.write(str(data))
    return f"file saves as {file_name}"

def get_data(item=None, url=URL):
    try:
        res = requests.get(url)
        data = json.loads(res.text)
        if item:
            data = data[item]
        return data
    except Exception as e:
        raise Exception(f"fail to get data from: {url}, error message: {e}")

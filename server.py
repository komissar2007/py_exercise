import datetime
import json

import web
import requests
from dicttoxml import dicttoxml

URL = "https://my-json-server.typicode.com/dim4iksh/test/db"

urls = (
    "/print_info",
    "Print",
    "/print_old",
    "PrintOld",
    "/to_xml",
    "ToXml",
    "/save_file",
    "SaveFile"
)
app = web.application(urls, globals())


def get_data(item=None, url=URL):
    res = requests.get(url)
    data = json.loads(res.text)
    if item:
        data = data[item]
    return data


class Print:
    def GET(self):
        print("Print")
        files = get_data('files')
        dict_info = {}
        for file in files:
            if not file['file_type'] in dict_info:
                dict_info[file['file_type']] = 1
            else:
                dict_info[file['file_type']] = dict_info[file['file_type']] + 1
        return f"number of each filetype in the db: \n{str(dict_info)}"


class PrintOld:
    def GET(self):
        files = get_data('files')
        oldest_file = None
        for file in files:
            if not oldest_file or datetime.datetime.strptime(oldest_file['date'],
                                                             "%d.%m.%y") > datetime.datetime.strptime(file['date'],
                                                                                                      "%d.%m.%y"):
                oldest_file = file
        return json.dumps(oldest_file, indent=4)


class ToXml:
    def GET(self):
        files = get_data('files')
        xml = dicttoxml(files)
        print(xml.decode('utf-8'))
        return xml


class SaveFile:
    def GET(self):
        data = get_data()
        ts = datetime.datetime.now().strftime("%d-%m-%Y%H_%M_%S")
        file_name = f"data_{ts}.json"
        with open(file_name, "w") as f:
            f.write(str(data))
        return f"file saves as {file_name}"


if __name__ == "__main__":
    app.run()

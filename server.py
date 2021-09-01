
import web

from utils import print_info, oldest_item, convert_to_xml, save_file



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

class Print:
    def GET(self):
        try:
            return print_info()
        except Exception as e:
            message = f"error to get info {e}"
            print(message)
            return message

class PrintOld:
    def GET(self):
        try:
            return oldest_item()
        except Exception as e:
            message = f"error to get info {e}"
            print(message)
            return message

class ToXml:
    def GET(self):
        try:
            return convert_to_xml()
        except Exception as e:
            message = f"error to get info {e}"
            print(message)
            return message

class SaveFile:
    def GET(self):
        try:
            return save_file()
        except Exception as e:
            message = f"error to get info {e}"
            print(message)
            return message


if __name__ == "__main__":
    app.run()

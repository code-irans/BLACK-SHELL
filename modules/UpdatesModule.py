import requests

def GetUpdate():
    url = "https://raw.githubusercontent.com/code-irans/killer_updater/main/update_list.txt"

    http = requests.get(url).text

    return http

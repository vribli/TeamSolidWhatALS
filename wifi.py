import subprocess
import re


def get_wifi_name():
    network_Information = str(subprocess.run(["iwgetid"]))
    name_search = re.search(r'ESSID:"(.*)"',network_Information)
    if name_search:
        result = name_search.group(0)
    else:
        result = "no_wifi"
        print(result)
        return result

if (__name__=='__main__'):
    get_wifi_name()

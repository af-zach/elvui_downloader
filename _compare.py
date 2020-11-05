from lxml import html
import requests

def get_public_version():        
    get_url = requests.get("https://www.tukui.org/download.php?ui=elvui")
    tree = html.fromstring(get_url.content)
    get_version = tree.xpath('//*[@id="version"]/b[1]/text()')

    ## Return version number as a list
    return get_version

def convert_list_to_float(version_list):
    ## Convert a list to a float
    for v in version_list:
        float_version = float(v)
    
    ## Return version number as a float
    return float_version

x = get_public_version()
y = convert_list_to_float(x)

print(x)
print(y)
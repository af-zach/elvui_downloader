from lxml import html
import requests
import _config

def get_public_version():   
    print('Checking public version.')     
    get_url = requests.get(_config.elvui_url)
    tree = html.fromstring(get_url.content)
    version_list = tree.xpath(_config.elvui_version_xpath)

    ## Convert version_list to a float
    get_version = convert_list_to_float(version_list)

    ## Return version number as a list
    return get_version

def get_local_version():
    print('Checking local version.')
    mylines = []
    ## Open ElvUI.toc store each line to a list 
    with open(_config.wow_addons+'/ElvUI/ElvUI.toc', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    version_line = mylines[2]
    myfile.close()
    
    ## Remove Version text characters and keep only version number
    string_version = version_line.replace('## Version: ', '')

    ## Convert string_version to a float
    get_version = float(string_version)

    return get_version

def convert_list_to_float(version_list):
    ## Convert a list to a float
    ## Will not work properly if more than one item in list
    for v in version_list:
        float_version = float(v)
    
    ## Return version number as a float
    return float_version


## Get public and local versions
x = get_local_version()
y = get_public_version()

## Compare versions
if x >= y:
    print('Your version of ElvUI is up to date.')
elif x < y:
    print('Needs updated')
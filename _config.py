## Input your path to local WOW addon folder
wow_addons = "E:/World of Warcraft/_retail_/Interface/AddOns/"

## Input your path to store downloaded versions of Elvui
save_path = "C:/Users/zach/Downloads/"

############################
## DO NOT EDIT BELOW HERE ##
############################

## Retail Elvui download page URL
elvui_url = "https://www.tukui.org/download.php?ui=elvui"

## Retail Elvui downloads URL
elvui_download_url = "https://www.tukui.org/downloads/"

## Elvui version XPath
elvui_version_xpath = '//*[@id="version"]/b[1]/text()'

from lxml import html
import requests
import zipfile
def get_public_version():        
    get_url = requests.get(elvui_url)
    tree = html.fromstring(get_url.content)
    version_list = tree.xpath(elvui_version_xpath)

    ## Convert version_list to a float
    get_version = convert_list_to_float(version_list)

    ## Return version number as a list
    return get_version

def get_local_version():
    mylines = []
    ## Open ElvUI.toc store each line to a list 
    with open(wow_addons+'/ElvUI/ElvUI.toc', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    
    ## Only keep the line which contains the version number
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

def download_elvui(url, save_path):
    ## Download the file contents in binary format
    r = requests.get(url)

    ## Open method to open a file on your system and write the contents
    with open(save_path, "wb") as code:
        code.write(r.content)

def unzip_elvui(path_to_zipfile, path_to_unzip):
    with zipfile.ZipFile(path_to_zipfile, 'r') as zip_ref:
        zip_ref.extractall(path_to_unzip)
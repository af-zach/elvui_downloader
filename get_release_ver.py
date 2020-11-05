from lxml import html
import requests

## Function to scrape released Elvui version
def check_version(x):
    get_url = requests.get(x)
    tree = html.fromstring(get_url.content)

    get_version = tree.xpath('//*[@id="version"]/b[1]/text()')

    ## Convert get_version from a list to a float
    for v in get_version:
        version = float(v)
    
    ## Finally return scrapped version string
    return version
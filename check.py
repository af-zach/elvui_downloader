import sys
import _config

## Get public and local versions
x = _config.get_local_version()
y = _config.get_public_version()

## Compare versions
if x < y:
    print('Your version of ElvUI is up to date. Goodbye :D')
    #sys.exit()
elif x >= y:
    ## Build path to file for download and path for saving
    url = _config.elvui_download_url + "elvui-" + str(y) + ".zip"
    save_path = _config.save_path + "elvui-" + str(y) + ".zip"

    ## Call function to download latest ElvUI
    print(f"Downloading ElvUI version {y}")
    _config.download_elvui(url, save_path)

    ## Call function to remove current ElvUI folders

    ## Call function to unzip new ElvUI version to wow/addons
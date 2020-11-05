import sys
import _config

## Get public and local versions
x = _config.get_local_version()
y = _config.get_public_version()

## Compare versions
if x >= y:
    print(f'Your version {x} of ElvUI is already up to date. Goodbye :D')
    sys.exit()
elif x < y:
    print("Your version of ElvUI needs updated.")
    ## Build path to file for download and path for saving
    url = _config.elvui_download_url + "elvui-" + str(y) + ".zip"
    save_path = _config.save_path + "elvui-" + str(y) + ".zip"

    ## Call function to download latest ElvUI
    print(f"Downloading ElvUI version {y}")
    _config.download_elvui(url, save_path)

    ## Call function to unzip new ElvUI version to wow/addons
    print(f"Unzipping elvui-{y}.zip to wow/addons")
    _config.unzip_elvui(save_path, _config.wow_addons)
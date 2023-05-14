import os
import glob

# match the subfolders with the correct app ('icns.iconset subfolder': 'default icon file name')
dictionary = {
   #'folder': 'AppName.app'
    'discord': 'Discord.app',
    'msteams': 'Microsoft Teams.app',
    'notion': 'Notion.app',
    'vscode': 'Visual Studio Code.app',
    'spotify': 'Spotify.app',
    'badlion': 'Badlion Client.app'
}

directory = './icns.iconset'

for filename in glob.glob(directory + '/*'): 

    
    #we are now seeing:
    #  ./icns.iconset/folder1/
    #  ./icns.iconset/folder2/
    #  ...

    # I need the dictionary key, which can be gotten by trimming out the './icns.iconset/' from filename
    FOLDER_NAME = filename[15:] 

    # to get the value (app name) from the json.
    APP_NAME = dictionary[FOLDER_NAME]

    # get the path for the app whose icon we're replacing by using the dictionary
    APP_PATH = f'/Applications/{APP_NAME}'

    # filename is ./icns.iconset/folder2, wildcard search for the new icon in each folder,
    # split up each parent folder and remove everything except the last one (which is the new .icns)
    NEW_ICON_FILE = glob.glob(filename + '/*.icns')[0].split('/')[-1]

    # default mac filepath for icons and apps in /Applications/...
    DEFAULT_ICON_PATH = f'/Applications/{APP_NAME}/Contents/Resources/{NEW_ICON_FILE}'

    # backup the existing .icns just to be safe
    os.system(f"sudo cp '{DEFAULT_ICON_PATH}' '{DEFAULT_ICON_PATH}.bak'")

    # replace the default icon file with the new one
    os.system(f"sudo cp '{filename}/{NEW_ICON_FILE}' '{DEFAULT_ICON_PATH}'")

    # reload
    os.system(f"sudo touch '{APP_PATH}'")

   
os.system("sudo rm -rf /Library/Caches/com.apple.iconservices.store")
os.system("killall Dock")
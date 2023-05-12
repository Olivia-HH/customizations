# What can I find here?
---
> Hey *[insert app here]*, can you please stop updating your icon to fit the look-and-feel of the new MacOS update?


Pretty soon, MS Teams and more of my everyday apps followed suit. I grew pretty tired of how it looked, since I previously spent a lot of time trying to customize my Macbook's LAF by hand.

I was getting annoyed, constantly having to manually replace the `.icns` files by hand every time an app updates their icon, so I decided to make my first Python script (originally written in bash): 

___

## An automatic `.icns` replacer
Sort of. It's a Python script, that's called by a bash script, that's run by a LaunchDaemon on startup for my computer. I added the Python script to help me scale up this process much quicker, seeing as more and more apps keep following suit of updating to match MacOS Montery-style icons. 

It's saved me hours of manually flipping through Finder to replace each individual icon. More importantly, it's saved me many *more* hours of trying to convince myself that I'm find with the new LAF of the default icons.


Using Python has helped me go from this:
```bash
#!/bin/sh
ICON_PATH=/Applications/<App1>.app/.../<Icon1>.icns
NEW_ICON_FILE=/Users/Olivia/.../<Icon1NEW>.icns
APP_PATH=/Applications/<App1>.app

sudo cp "${ICON_PATH}" "${ICON_PATH}.bak"
sudo cp "${NEW_ICON_FILE}" "${ICON_PATH}"
sudo touch "${APP_PATH}"


ICON_PATH=/Applications/<App2>.app/.../<Icon2>.icns
NEW_ICON_FILE=/Users/Olivia/.../<Icon2NEW>.icns
APP_PATH=/Applications/<App2>.app

sudo cp "${ICON_PATH}" "${ICON_PATH}.bak"
sudo cp "${NEW_ICON_FILE}" "${ICON_PATH}"
sudo touch "${APP_PATH}"

# Repeat for 20 apps...
```

To a much more handy, iterative, sanity-preserving solution:

```python
# All I need to do now is simply update a key-value pair!
dictionary = {
   #'folder': 'AppName.app'
    'folder1': 'App1.app',
    'folder2': 'App2.app',
    'folder3': 'App3.app',
    # ...
}

directory = './icns.iconset'

for filename in glob.glob(directory + '/*'): 

    FOLDER_NAME = ...

    APP_NAME = ...

    APP_PATH = ...

    NEW_ICON_FILE = ...

    # default mac filepath for icons and apps in /Applications/...
    DEFAULT_ICON_PATH = f'/Applications/{APP_NAME}/Contents/Resources/{NEW_ICON_FILE}'

    # backup the existing .icns just to be safe
    os.system(f"sudo cp '{DEFAULT_ICON_PATH}' '{DEFAULT_ICON_PATH}.bak'")

    # replace the default icon file with the new one
    os.system(f"sudo cp '{filename}/{NEW_ICON_FILE}' '{DEFAULT_ICON_PATH}'")

    # reload
    os.system(f"sudo touch '{APP_PATH}'")


```

---

## How does it work?

Uses a specific file structure pattern and Python dictionary to iteratively overwrite each `.icns` in the default `/Application/...` folder on MacOS. 

All that needs to be provided is:
- Your new `.icns` file
- The file name the app developer uses for the default `.icns` file
- The package name the app developer uses for their app

And voila! 
```
icns.iconset/
├── folder1/
│   ├── app1.icns
│
├── folder2/
│   ├── app2.icns
│
├── folder3/
│   ├── app3.icns
│
├── folder4/
│   ├── app4.icns
│
...
```

Following this directory tree, we can easily set up hundreds of apps' icons to automatically re-theme on startup. No more manually overwriting!

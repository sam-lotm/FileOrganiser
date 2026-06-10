import os
import datetime
now = datetime.datetime.now()

class FRead():

    rootDir = "D:\\"
    counts = {"Folder": 0,"Logism": 0, "Image": 0, "Documents": 0, "Applications": 0, "Sound": 0, "Other": 0}

    for files in rootDir:
        name, ext = os.path.splitext(rootDir)
        ext = ext.lower()

        if ext in ['.circ']:
            category = 'Logism'
        elif ext in ['.jpeg', '.png']:
            category = 'Image'
        elif ext in ['.docx', '.pdf', '.txt']:
            category = 'Documents'
        elif ext in ['.exe']:
                category = 'Applications'
        elif ext in ['.mp4']:
            category = 'Sound'
        else:
            category = 'Other'

        counts[category] += 1
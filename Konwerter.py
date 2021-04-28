import os
import traceback

from PIL import Image

type = input("Wich file type do you want?")

strdir = input('Provide abslute path to your files')
dir = os.listdir(strdir)
strretdir = input('Provide absolute path for converted files')
retdir = os.listdir(strretdir)
for filename in dir:
    print(filename)
    try:
        im = Image.open(os.path.join(strdir, filename))
        filename = filename.split('.')[0] + '.' + type
        im.save(os.path.join(strretdir, filename))
        print('File converted')
    except PermissionError:
        print('That\'s an File Folder not a File')
    except:
        print('Couldn\'t convert file')
        traceback.print_exc()

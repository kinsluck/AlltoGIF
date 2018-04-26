import os
import glob
from PIL import Image


def im_resizer(self):
    percent = int(input('Input the resizing percent: '))/100
    x, y = Image.open(self).size
    new_size = Image.open(self).resize((int(percent*x), int(percent*y)))
    return new_size


included_ext = ('jpg', 'jpeg', 'bmp', 'png', 'gif',
                'eps', 'icns', 'ico',  'tif', 'tiff',
                'exif', 'j2p', 'jpx', 'xpm', 'jp2',
                'j2k', 'jxr', 'hdp'
                )

for infile in os.listdir('.'):
    if infile.endswith(included_ext):
        f, e = os.path.splitext(infile)
        outfile = f + ".gif"
        if infile != outfile:
            print('The operated file by now is: %s.' % infile)
            newfile = im_resizer(infile)
            newfile.save(outfile)
    else:
        print('Not the extension that can be proceeded')

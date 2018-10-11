"""
download the images from urls

you can get urls by https://www.chrisains.com/seo-tools/extract-urls-from-image-serps/
"""


import urllib.request
import sys
import os


img_folder = os.path.join(os.path.sep, '')

if not os.path.exists(img_folder):
    print('make dir ', img_folder)
    os.makedirs(img_folder)
else:
    print('error, the dir already exists')
    exit()

with open('urls', 'r') as r:
    counter = 0
    for line in r.readlines():
        try:
            print(line)
            response = urllib.request.urlopen(line, timeout=3)
            image = response.read()
            img_name = line.split('/')[-1][:-1]
            if not img_name.endswith(('.jpg', 'jpeg','.png', '.bmp', '.JPG', 'JPEG','.PNG', '.BMP')):
                img_name = img_name + '.jpg'
            with open(os.path.join(img_folder, img_name), 'wb') as f:
                f.write(image)
                counter += 1
                f.close()
        except:
            print('can not access ', line)

    print('finished with {} downloaded'.format(counter))


# -*- coding: utf-8 -*-
import os
import zipfile

DIRETORIO_RAIZ = '.'

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

for dirname, dirnames, filenames in os.walk(DIRETORIO_RAIZ):
    for filename in filenames:

        if '.png' in filename:

            file_path = os.path.join(dirname, filename)

            command = 'convert -resize 50%% %s %s' % (file_path, file_path)

            os.system(command)
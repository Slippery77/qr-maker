import pyqrcode

name = 'Im in love with you'
k = pyqrcode.create(name)
k.png('test.png',scale=10)

import os
os.system('test.png')

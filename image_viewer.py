#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

# Open and transform image
img = Image.open(image_file)
img = img.rotate(90, expand=True)
w, h = img.size
x_tr = 65
img = img.crop((0, x_tr, w, w / 2 + x_tr)) 
img = img.resize((64, 32))
img = img.convert('RGB')

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

# Display image on the matrix
matrix = RGBMatrix(options = options)
matrix.SetImage(img)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)

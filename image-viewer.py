#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

IMAGE_RATIO = 2

image = Image.open(image_file)
#image = image.rotate(90)

width, height = image.size
image = image.rotate(90)

image = image.crop((0, 0, width, width * 2))
image = image.resize((64, 32))

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)

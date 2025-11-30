# Demonstrates lazy loading of images from a folder using a generator to process one at a time.

import os

from PIL import Image


def image_stream(folder):
    for file in os.listdir(folder):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            yield Image.open(os.path.join(folder, file))


# Usage
for img in image_stream("../images"):
    print(img.size)
    img.close()  # Close images after use

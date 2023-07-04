import numpy as np
from PIL import Image
import os

max_iter = 80

img = Image.new(mode='P', size=(600, 600), color=(150, 237, 137))


def mandelBrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


if __name__ == "__main__":
    for a in range(0, 450):
        for b in range(0, 500):
            x = (a - 300) / 150
            y = (b - 300) / 150
            if 0 < mandelBrot(complex(x, y)) <= 2:
                img.putpixel((a, b), (150, 237, 137))
            if 2 < mandelBrot(complex(x, y)) <= 3:
                img.putpixel((a, b), (69, 191, 85))
            if 3 < mandelBrot(complex(x, y)) <= 5:
                img.putpixel((a, b), (22, 128, 57))
            if 5 < mandelBrot(complex(x, y)) <= 10:
                img.putpixel((a, b),(4, 77, 41))
            if 10 < mandelBrot(complex(x, y)) <= 15:
                img.putpixel((a, b), (0, 38, 28))
            if 15 < mandelBrot(complex(x, y)) <= 80:
                img.putpixel((a, b), (0, 0, 0))

img.save('output.png')
os.startfile('output.png')

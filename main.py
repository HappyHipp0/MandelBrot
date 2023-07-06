import os

from PIL import Image

max_iter = 80

img = Image.new(mode='P', size=(600, 600), color=(22, 88, 73))

colors = [(23, 89, 74), (36, 107, 62), (63, 119, 50), (99, 123, 48), (142, 122, 61), (177, 122, 89),
          (203, 124, 129), (213, 133, 173), (255, 255, 255), (0, 0, 0)]


def mandelBrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


def assignColors(x, y):
    global colors

    ranges = [0, 1, 2, 3, 5, 7, 10, 15, 30, 60, max_iter]

    for i in range(len(ranges) - 1):
        if ranges[i] < mandelBrot(complex(x, y)) <= ranges[i + 1]:
            return colors[i]

    return None


if __name__ == "__main__":
    for a in range(0, 600):
        for b in range(0, 600):
            x = (a - 300) / 150
            y = (b - 300) / 150
            color = assignColors(x, y)
            if color is not None:
                img.putpixel((a, b), color)

img.save('output.png')
os.startfile('output.png')

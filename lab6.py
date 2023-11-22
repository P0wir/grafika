from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('obraz.jpg')
print("tryb obrazu", obraz.mode)
print("rozmiar", obraz.size)


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, maska, m, n, kolor):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                obraz1.putpixel((i + m, j + n), (kolor))
    return obraz1

inicjaly = Image.open('inicjaly.bmp')

obraz1 =  wstaw_inicjaly(obraz, inicjaly, obraz.width - inicjaly.width, obraz.height - inicjaly.height, (255,0,0))
obraz1.save('obraz1.jpg')

def wstaw_inicjaly_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1

obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, obraz.width//2, obraz.height//2, 255, -100, 0)
obraz2.save('obraz2.jpg')

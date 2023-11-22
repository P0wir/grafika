from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('obraz.jpg')
print("tryb obrazu", obraz.mode)
print("rozmiar", obraz.size)


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def change_color(image, target_color, replacement_color):
    data = image.getdata()
    new_data = [replacement_color if pixel == target_color else pixel for pixel in data]
    new_image = Image.new("RGB", image.size)
    new_image.putdata(new_data)
    return new_image

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w_inicjalow, h_inicjalow = inicjaly.size
    modified_inicjaly = change_color(inicjaly, (0, 0, 0), (255, 0, 0))
    obraz_copy = obraz.copy()
    obraz_copy.paste(modified_inicjaly, (m, n))
    return obraz_copy

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz_copy = obraz.copy()

    m_centered = m + (obraz.width - inicjaly.width) // 2
    n_centered = n + (obraz.height - inicjaly.height) // 2

    w_inicjalow, h_inicjalow = inicjaly.size
    for i in range(w_inicjalow):
        for j in range(h_inicjalow):
            if i + m_centered < obraz.width and j + n_centered < obraz.height:
                mask_pixel = inicjaly.getpixel((i, j))
                if mask_pixel == (0, 0, 0):
                    image_pixel = obraz_copy.getpixel((i + m_centered, j + n_centered))
                    new_pixel = (
                        max(0, min(255, image_pixel[0] + x)),
                        max(0, min(255, image_pixel[1] + y)),
                        max(0, min(255, image_pixel[2] + z)),
                    )
                    obraz_copy.putpixel((i + m_centered, j + n_centered), new_pixel)

    return obraz_copy


obraz = Image.open('obraz.jpg')
inicjaly = Image.open('inicjaly.bmp').convert('RGB')

red_color = (255, 0, 0)

obraz1 = wstaw_inicjaly(obraz, inicjaly, obraz.width - inicjaly.width, obraz.height - inicjaly.height, red_color)
obraz1.save('obraz1.jpg')

x, y, z = 50,50,50

obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, 0, 0, x, y, z)
obraz2.save('obraz2.jpg')

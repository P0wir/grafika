from PIL import Image
import math

im = Image.open('snieg.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def rysuj_kwadrat_max(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = max(temp[0], pixel[0])
            temp[1] = max(temp[1], pixel[1])
            temp[2] = max(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

im = im.copy()
kwadrat1 = rysuj_kwadrat_max(im, 100, 200, 25)
kwadrat2 = rysuj_kwadrat_max(kwadrat1, 175, 200, 39)
kwadrat3 = rysuj_kwadrat_max(kwadrat2, 250, 200, 51)
kwadrat3.save('obraz1.png')

def rysuj_kwadrat_min(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = min(temp[0], pixel[0])
            temp[1] = min(temp[1], pixel[1])
            temp[2] = min(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

im2 = im.copy()
kwadrat1a = rysuj_kwadrat_min(im, 100, 200, 25)
kwadrat2a = rysuj_kwadrat_min(kwadrat1a, 175, 200, 39)
kwadrat3a = rysuj_kwadrat_min(kwadrat2a, 250, 200, 51)
kwadrat3a.save('obraz2.png')


def kopiuj_kolo(obraz, m, n, r, m1, n1):
    obraz1 = obraz.copy()
    w, h = obraz.size

    for i in range(w):
        for j in range(h):
            if (i - m) ** 2 + (j - n) ** 2 < r ** 2:
                p = obraz.getpixel((i, j))
                obraz1.putpixel((i + m1 - m, j + n1 - n), p)

    return obraz1

def rysuj_kolo(obraz, m, n, r, k1, b1):
    obraz1 = obraz.copy()
    w, h = obraz.size

    for i in range(w):
        for j in range(h):
            if (i - m) ** 2 + (j - n) ** 2 < r ** 2:
                kolor = obraz.getpixel((k1, b1))
                obraz1.putpixel((i + m, j + n), kolor)

    return obraz1

im3 = im.copy()
obraz4 = kopiuj_kolo(im3, 721, 506, 50, 10, 10)
obraz4.save('obraz4.png')

im4=im.copy()
obraz3 = rysuj_kolo(im4, 200, 200, 50, 400, 400)
obraz3.save('obraz3.png')

from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

im1 = Image.open('obraz.jpg')

r, g, b = im1.split()

permutacje = [g, b, r]
im3 = Image.merge('RGB', permutacje)
im3.save("im3.png")

im3_png = Image.open("im3.png")

diff_png = ImageChops.difference(im1, im3_png)

diff_png.save("diff.png")


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


statystyki(diff_png)

hist1 = diff_png.histogram()
p = 0
print(hist1[p])
print(hist1[256 + p])
print(hist1[2 * 256 + p])


def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


rysuj_histogram_RGB(diff_png)


def zlicz_roznice_srednia_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


def zlicz_roznice_suma_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:  # poniżej równoważne sformułowania tego warunku
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


wsp = 5
zlicz, procent = zlicz_roznice_srednia_RGB(diff_png, wsp)
print('liczba niepasujących pikseli = ', zlicz)
print('procent niepasujących pikseli = ', procent)
zlicz1, procent1 = zlicz_roznice_suma_RGB(diff_png, wsp)
print('liczba niepasujących pikseli = ', zlicz1)
print('procent niepasujących pikseli = ', procent1)

im1.save('obraz2.jpg')
im2 = Image.open("obraz2.jpg")
im2.save('obraz3.jpg')
im3 = Image.open("obraz3.jpg")
im3.save('obraz4.jpg')
im4 = Image.open("obraz4.jpg")
im4.save('obraz5.jpg')
im5 = Image.open('obraz5.jpg')

difference = ImageChops.difference(im1, im5)
difference2 = ImageChops.difference(im4, im5)
difference.save("diff15.jpg")
difference2.save('diff45.jpg')
zlicz_roznice_srednia_RGB(difference2, wsp)


def dekoduj_kod(kodowany_obraz, oryginalny_obraz):
    t_kodowany = np.asarray(kodowany_obraz)
    h, w, d = t_kodowany.shape
    t_oryginalny = np.asarray(oryginalny_obraz)
    t_odkodowany = t_kodowany.copy()
    for i in range(h):
        for j in range(w):
            if t_oryginalny[i, j] > 0:
                k = np.argmax(t_kodowany[i, j, :])
                t_odkodowany[i, j, k] = t_kodowany[i, j, k] - 1
    return Image.fromarray(t_odkodowany)


jesien = Image.open('zakodowany1.bmp')
jesienorg = Image.open('jesien.jpg')

dekodowany = dekoduj_kod(jesien, jesienorg)
dekodowany.save('jesieen.jpg')

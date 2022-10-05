from PIL import Image  # Python Imaging Library
import numpy as np

obrazek2 = Image.open("inicjaly.bmp")
obrazek2.show()
print("---------- informacje o inicjalach")
print("tryb:", obrazek2.mode)
print("format:", obrazek2.format)
print("rozmiar:", obrazek2.size)

dane_obrazka = np.asarray(obrazek2)
dane_obrazka1 = dane_obrazka * 1
print(dane_obrazka1)
ob_d = Image.fromarray(dane_obrazka1)
ob_d.show()

inicjaly = open('inicjaly.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        inicjaly.write(str(item) + ' ')
    inicjaly.write('\n')


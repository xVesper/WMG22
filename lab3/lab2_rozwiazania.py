from PIL import Image
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def wstaw_obraz(obraz_wstawiany, w_m, h_m,wsp,w0,h0):
    dane_obrazka = np.asarray(obraz_wstawiany)
    dane_obrazka1 = dane_obrazka * 1
    if wsp>1:
        rozmiar_duzego_obrazu_width = wsp*w0
        rozmiar_malego_obrazu_height = wsp*h0
    duzy_obraz = np.zeros((rozmiar_malego_obrazu_height,rozmiar_duzego_obrazu_width), dtype=int)
    for x in range(h0):
        for y in range(w0):
            duzy_obraz[x+w_m][y+h_m]=dane_obrazka1[x][y]
    duzy_obraz = duzy_obraz * 255
    obraz = Image.fromarray(duzy_obraz)
    obraz=obraz.convert('RGB')
    obraz.save("duzy_obraz3.bmp") 


def zad_3_pp1(w,h,dzielnik):
    t = (h,w)
    tab = np.zeros(t, dtype=np.uint8)  
    grubosc_ramki = int(min(w, h) / dzielnik)  
    z1 = h - grubosc_ramki
    z2 = w - grubosc_ramki
    tab[grubosc_ramki:z1, grubosc_ramki:z2] = 1 
    tab[grubosc_ramki + grubosc_ramki:z1 - grubosc_ramki, grubosc_ramki + grubosc_ramki:z2 - grubosc_ramki] = 0
    tab[grubosc_ramki + grubosc_ramki*2:z1 - grubosc_ramki*2, grubosc_ramki + grubosc_ramki*2:z2 - grubosc_ramki*2] = 1
    tab[grubosc_ramki + grubosc_ramki*3:z1 - grubosc_ramki*3, grubosc_ramki + grubosc_ramki*3:z2 - grubosc_ramki*3] = 0
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("zad_3a.bmp")
    obraz.show() 

def zad_3_pp2(w, h, dzielnik): 
    t = (w, h)  
    tab = np.ones(t, dtype=np.uint8)
    grubosc_ramki = int(h / dzielnik)  
    print(grubosc_ramki)
    for k in range(dzielnik): 
        for g in range(grubosc_ramki):
            i = k * grubosc_ramki + g  
            for j in range(w):
                tab[j, i] = k % 2  
    tab = tab * 255 
    obraz = Image.fromarray(tab)  
    obraz.save("zad_3_pp2_odd.bmp")
    obraz.show()

def zad_3_pp3(w,h,m,n):
    t = (h,w)
    tab = np.ones(t,dtype=np.uint8)
    tab[0:n,0:m]=0
    tab[n:w,m:h]=0
    tab*=255
    obraz = Image.fromarray(tab)
    obraz.save("zad_3_pp3_odd.bmp")
    obraz.show()


def zad_3_pp4(w, h): 
    times = h
    prymes = w
    duzy_obraz = np.zeros((h,w), dtype=int)
    duzy_obraz[h//4:h,w//2:w]=1
    while(times>0):
        duzy_obraz[-times:h,0:-prymes]=1
        times-=5
        prymes-=10
    duzy_obraz[h//2:h,w//2:w]=0
    duzy_obraz*=255
    obraz = Image.fromarray(duzy_obraz)
    obraz=obraz.convert('RGB')
    obraz.save("zad_4_pp4_odd.bmp")
    #obraz.show()


obrazek = Image.open("inicjaly.bmp")
wstaw_obraz(obrazek,100,200,3,100,50)
zad_3_pp1(120,50,22)
zad_3_pp2(320,480,25)
zad_3_pp3(120,60,50,20)

#zad_3_pp4(320,480)
obrazek = Image.open("zad_3_pp1_odd.bmp")
obrazek1 = Image.open("zad_3_pp2_odd.bmp")
obrazek2 = Image.open("zad_3_pp3_odd.bmp")
obrazek3 = Image.open("zad_4_pp4_odd.bmp")
zmiksuj(obrazek, obrazek1,obrazek2,obrazek3,480,320)
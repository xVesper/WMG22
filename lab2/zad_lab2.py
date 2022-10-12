from PIL import Image
import numpy as np

obraz = Image.open("lab1/inicjaly.bmp")
#Zadanie 1
print("\ntryb:", obraz.mode)
print("format:", obraz.format)
print("rozmiar:", obraz.size)

t_obraz = np.asarray(obraz)
print("\ntyp danych tablicy:", t_obraz.dtype)
print("rozmiar tablicy:", t_obraz.shape)


def wstaw_obraz(t_obraz):
    h_m,w_m=t_obraz.shape
    print(h_m,w_m)
    t=(2*h_m,2*w_m)
    tab=np.zeros(t,dtype=np.uint8)
    for i in range(25,25+h_m-1):
        for j in range(50,50+w_m-1):
            tab[i][j]=t_obraz[i-25][j-50]
    tab=tab.astype(bool)
    obraz_wstawiony=Image.fromarray(tab)
    return obraz_wstawiony

po_wstawieniu=wstaw_obraz(t_obraz)
#po_wstawieniu.show()

#Zadanie2

def wstaw_obraz2(obraz_wstawiany, h_m, w_m, wsp):
    h, w = obraz_wstawiany.shape
    t = (int(round(wsp*h,0)), int(round(wsp*w,0)))
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h_m, min(h_m+h-1, int(round(wsp*h, 0)))):
        for j in range(w_m, min(w_m+w-1, int(round(wsp*w)))):
            tab[i][j]=obraz_wstawiany[i-h_m][j-w_m]
    tab = tab.astype(bool)
    cos = Image.fromarray(tab)
    return cos

a=wstaw_obraz2(t_obraz, 60, 115, 2.5)
b=wstaw_obraz2(t_obraz, 150, 395, 13)
c=wstaw_obraz2(t_obraz, 1000, 1105, 50)
#a.show()
#b.show()
#c.show()

#zadanie3

def obraz1(w,h,dzielnik):
    t=(h,w)
    tab=np.zeros(t,dtype=np.uint8)
    grub=int(min(w,h)/dzielnik)
    z1=h-grub
    z2=w-grub
    tab[grub:z1,grub:z2]=1
    tab[grub+grub:z1-grub,grub+grub:z2-grub]=0
    tab[grub+grub*2:z1-grub*2,grub+grub*2:z2-grub*2]=1
    tab[grub+grub*3:z1-grub*3,grub+grub*3:z2-grub*3]=0
    return tab*255

tab=obraz1(120, 60, 8)
zad51=obraz1(480, 320, 8)
im_ramka=Image.fromarray(tab)
z51=Image.fromarray(zad51)
z51.save("lab1/zad51.bmp")
#im_ramka.show()
#z51.show()


def obraz2(w, h, dzielnik):
    t = (w, h)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.show()
#obraz2(400, 630, 9)
obraz2(480, 320, 8)
obraz.save("lab1/zad52.bmp")

def obraz3(m,n,w,h):
    t=(h,w)
    tab=np.ones(t,dtype=np.uint8)
    tab[0:int(m/2),0:int(n/2)]=0
    tab[int(h/2):h,int(w/2):w]=0
    return tab*255

tab = obraz3(50,20,120,60)
tab1 = obraz3(10,20,120,60)
zad53=obraz3(480,320,100,50)
im_ramka = Image.fromarray(tab)
im_ramka1 = Image.fromarray(tab1)
z53=Image.fromarray(zad53)
z53.save("lab1/zad53.bmp")
#im_ramka.show()
#im_ramka1.show()
#z53.show()

def obraz4(w,h,dzielnik):
    t=(h,w)
    tab=np.zeros(t,dtype=np.uint8)
    grub=int(min(w,h)/dzielnik)
    z1=h-grub
    z2=w-grub
    tab[grub:z1,grub:z2]=1
    tab[grub+grub:z1-grub,grub+grub:z2-grub]=0
    tab[grub+grub*2:z1-grub*2,grub+grub*2:z2-grub*2]=1
    tab[grub+grub*3:z1-grub*3,grub+grub*3:z2-grub*3]=0
    tab[grub + grub * 5:z1 - grub * 5, grub + grub * 5:z2 - grub * 5] = 1
    tab[grub + grub * 3:z1 - grub * 3, grub + grub * 3:z2 - grub * 3] = 0
    tab[grub + grub * 2:z1 - grub * 2, grub + grub * 2:z2 - grub * 6] = 1
    tab[grub + grub * 6:z1 - grub * 6, grub + grub * 3:z2 - grub * 3] = 1
    tab[grub + grub * 10:z1 - grub * 10, grub + grub * 10:z2 - grub * 10] = 0
    tab[grub + grub * 6:z1 - grub * 6, grub + grub * 16:z2 - grub * 3] = 1
    tab[grub + grub * 4:z1 - grub * 4, grub + grub * 14:z2 - grub * 8] = 1
    tab[grub + grub * 50:z1 - grub * 50, grub + grub * 50:z2 - grub * 50] = 0
    return tab*255

tab=obraz4(600, 1600, 110)
im_ramka=Image.fromarray(tab)
#im_ramka.show()
zad54=obraz4(480, 320, 8)
z54=Image.fromarray(zad54)
z54.save("lab1/zad54.bmp")
#z54.show()
import numpy as np
from PIL import Image
# def wstaw_obraz(obraz_wstawiany,w_m,h_m,wsp):
#     dane_obrazka = np.asarray(obraz_wstawiany)
#     t = (wsp*h_m,wsp*w_m)
#     tab = np.zeros(t,dtype=np.uint8)
#     for i in range(25, 25 + h_m - 1):
#         for j in range(50, 50 + w_m - 1):
#             tab[i][j] = obraz_wstawiany[i - 25][j - 50]
#     tab.astype(bool)
#     xd = Image.fromarray(tab)
#     xd.show()
    
# wstaw_obraz("bs.bmp", 100, 150, 2)


# def wstaw_obraz(obraz_wstawiany):
# h_m, w_m = obraz_wstawiany.shape
# wsp = 2
# t = (wsp * h_m, wsp * w_m)
# tab = np.zeros(t, dtype=np.uint8)

# for i in range(25, 25 + h_m - 1):
# for j in range(50, 50 + w_m - 1):
# tab[i][j] = obraz_wstawiany[i - 25][j - 50]
# tab = tab.astype(bool)
# po_wstawieniu = Image.fromarray(tab)
# return po_wstawieniu
# po_wstawieniu = wstaw_obraz(t_inicjaly)
# po_wstawieniu.show()

def ob1(w,h,dzielnik):
    t = (h,w)
    tab = np.zeros(t, dtype=np.uint8)  
    grub = int(min(w, h) / dzielnik)  
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 1 
    tab[grub + grub:z1 - grub, grub + grub:z2 - grub] = 0
    tab[grub + grub*2:z1 - grub*2, grub + grub*2:z2 - grub*2] = 1
    tab[grub + grub*3:z1 - grub*3, grub + grub*3:z2 - grub*3] = 0
    return tab * 255 

def ob2(w, h, dzielnik): 
    t = (w, h)  
    tab = np.ones(t, dtype=np.uint8)
    grub = int(h / dzielnik)  
    print(grub)
    for k in range(dzielnik): 
        for g in range(grub):
            i = k * grub + g  
            for j in range(w):
                tab[j, i] = k % 2  
    tab = tab * 255 
    obraz = Image.fromarray(tab)  
    obraz.show()

#tab = ob1(120, 60, 10)
tab2 = ob2(300,200,8)

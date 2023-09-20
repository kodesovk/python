
from util import tah
from ai import tah_pocitace 


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo"in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole, symbol):
    while True:    
        pozice= int(input("Zadej číslo pole, na které chceš hrát. (od 0 až po 19):"))
        if pozice >= 0 and pozice <= 19 and pole[pozice] == "-":
            return tah(pole, pozice, symbol)
        else:
            print("Zadala jsi neplatný údaj, zkus to znovu.")

def piskvorky1d():
    pole= 20*"-"
    while True: 
        pole = tah_hrace(pole,"x")
        print(pole)
        pole= tah_pocitace(pole)
        print(pole)

        vyhodnoceni= vyhodnot(pole)
        print(vyhodnoceni)
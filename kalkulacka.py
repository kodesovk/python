def soucet(a,b):
    return a + b

if __name__=="__main__": # tímto se dá předcházet, když toto nechceme použivat , když si to zavoláme ( nezeptá se nás na to)
    a = float(input("Zadej mi cislo a:"))
    b = float(input("Zadej mi cislo b:"))

    print("soucet", a, "a", b, "b","je", soucet(a,b))


# když to bude v jiné složce, tak např. import moduly.kalkulacka as k.
#pycache se dá smazat..nic se nestane, vytvoři se znova, až to zas naimportujeme
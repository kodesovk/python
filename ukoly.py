# Napiš funkci, do které se vloží dvě čísla a ona vrátí jejich podíl. 
# Pokud dojde na dělení nulou, tak vyhodí výjimku "Nulou dělit nelze!".

def deleni(a,b):
    try:
         return a//b
    except ZeroDivisionError:
        print("Nulou dělit nelze.")

print(deleni(5,0))


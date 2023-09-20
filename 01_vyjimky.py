# def deleni(a,b):
#     return a/b

# print(deleni(10,0))

# try:
#     print(deleni(10,0))
# except ZeroDivisionError:
#     print("Delit nulou neumim.")

#     print("10 deleno 5", deleni(10,2))


# while True:
#     try:    
#         vek = int(input("Zadej svuj vek:"))
#     except ValueError:
#         print("Věk musí být číslo.")
#         continue
#     break

# while True:
#     try:    
#         vek = int(input("Zadej svuj vek:"))
#         vek/0
#     except ValueError:
#         print("Věk musí být celé číslo.")
#     except ZeroDivisionError:
#         print("Nulou dělit nelze.")
#     else:
#         break

# while True:
#     try:    
#         vek = int(input("Zadej svuj vek:"))
#         vek/0
#     except ValueError:
#         print("Věk musí být celé číslo.")
#     except ZeroDivisionError:
#         print("Nulou dělit nelze.")
#     except Exception:
#         print("Nastala jiná vyjimka.")
#     else:
#         pass
#     finally:
#         print("Provede se vždy.")
#     break
# # zadame exception


# while True:
#     try:
#         a = float(input("Zadej první stranu obdélníka (a): "))
#         if a <= 0:
#             print("Délka nemůže být záporná!")
#             continue
#     except ValueError:
#         print("Zadej cislo.")
#         continue
#     except Exception:
#         print("Stala se jiná chyba.")
#     break

# while True:
#     try:
#         b = float(input("Zadej druhou stranu obdélníka (b): "))
#         if b <= 0:
#             print("Délka nemůže být záporná!")
#             continue
#     except ValueError:
#         print("Zadej cislo.")
#         continue
#     except Exception:
#         print("Stala se jiná chyba.")
#     break

# while True:
#     try:
#         a = float(input("Zadej první stranu obdélníka: "))
#         b = float(input("Zadej druhou stranu obdélníka: "))
#         if a <= 0 or b <= 0:
#             print("Délka nemůže být záporná!")
#             continue
#         break
#     except ValueError:
#         print("Zadej cislo.")
    
while True:
    try:
        a = float(input("Zadej první stranu obdélníka: "))
        b = float(input("Zadej druhou stranu obdélníka: "))
        if a <= 0 or b <= 0:
            raise ValueError("Délka nemůže být záporna") # lze i jen prázdné závorky 
            print("Délka nemůže být záporná!")
            continue
        break
    except ValueError:
        print("Strana musí být kladné cislo.")
    
        
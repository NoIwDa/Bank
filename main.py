from pathlib import Path
#sprawdz czy plik istnieje
#jesli istnieje to go otworz
#jesli nie istnieje to go stwoz

def stworz_konto():
    with open(plik_nazwa, 'w') as file:
        pass

def zapisz_saldo(nowe_saldo: float):
    with open(plik_nazwa, 'w') as file:
        file.write(str(nowe_saldo))
    print(f"Nowe saldo {nowe_saldo} PLN zapisano w pliku.")


def sprawdz_saldo():
    with open(plik_nazwa, 'r') as file:
        saldo = file.read()
    return float(saldo) if saldo else 0.0  # Zwracaj wartość numeryczną


def dodaj_do_salda(dodawana_kwota:float)->float:
    nowe_saldo = sprawdz_saldo() + float(dodawana_kwota)
    return nowe_saldo


def odejmij_od_salda(odejmij:float)->float:
    nowe_saldo = sprawdz_saldo()-float(odejmij)
    return nowe_saldo



nr_klienta = int(input(" Podaj Nr klienta: "))
nr_klienta = str(nr_klienta)
plik_nazwa = nr_klienta + ".txt"
plik = Path(plik_nazwa)

if plik.is_file():
    print("Konto istnieje!")
else:
    print("Konto nie istnieje")

while plik.is_file() == "False":
    print("Czy utworzyc konto?")
    a = input("T/N?").upper()
    if a == "T":
        stworz_konto()
    else:
        print("Nie to nie. Dowidzenia")
        quit()





# with open(plik_nazwa,'w') as file:
#     pass
#
#
# def sprawdz_saldo():
#     with open(plik_nazwa,'r') as file:
#         print(file.read())

# def zapisz_saldo(nowe_saldo: float):
#     with open(plik_nazwa, 'w') as file:
#         file.write(str(nowe_saldo))
#     print(f"Nowe saldo {nowe_saldo} PLN zapisano w pliku.")
#
#
# def sprawdz_saldo():
#     with open(plik_nazwa, 'r') as file:
#         saldo = file.read()
#     return float(saldo) if saldo else 0.0  # Zwracaj wartość numeryczną
#
#
# def dodaj_do_salda(dodawana_kwota:float)->float:
#     nowe_saldo = sprawdz_saldo() + float(dodawana_kwota)
#     return nowe_saldo
#
#
# def odejmij_od_salda(odejmij:float)->float:
#     nowe_saldo = sprawdz_saldo()-float(odejmij)
#     return nowe_saldo
#
while True:
    wybor = input("Witaj w banku. Co chcesz zrobic? 1 - sprawdzic saldo, 2 - wplaici, 3 - wyplacic 4 - Zakonczyc").upper()
    if wybor == "1":
        print(sprawdz_saldo())
    elif wybor == "2":
       print("Twoje obecne saldo wynosi: ",sprawdz_saldo())
       a = input("Ile chcesz wplacic?")
       zapisz_saldo(dodaj_do_salda(a))
       print("Nowy stan salda to: ", sprawdz_saldo())
    elif wybor == "3":
        print("Twoje obecne saldo wynosi: ", sprawdz_saldo())
        a = input("Ile chcesz wyplacic?")
        zapisz_saldo(odejmij_od_salda(a))
        print("Nowy stan salda to: ", sprawdz_saldo())
    elif wybor == "4":
        print("Do widzenia :D")
        break

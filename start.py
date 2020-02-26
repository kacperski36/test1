print("Hello World")

# komentarz ctrl + / lub (#)

# def funkcja():
#     print('xd')
#     a=7
#     imie="Zbyszko"

a=5
print(type(a))
# <class 'int'>
imie = "Ala"
imie = 'Ala'
imie = """Ala
ma kota
filemona"""

print(type(imie))
imie=6
print(type(imie))
imie=6.3
print(type(imie))

# def funkcje():
#     """docstring"""
#     pass

# liczba=string(5)
# liczba=int("5")
# liczba=int("5.5")

imie="ala"
print(imie.capitalize())
imie=imie.capitalize()
print(imie)
print(imie[0])
# imie[0]="a" błąd
print("ala".capitalize().count("A"))

print(imie + imie)
# print(5 + imie) błąd
#formatowanie wyjscia
print("Ala ma 5 lat")
# print("Ala" + "ma"+5+"lat") błąd
print(imie + " ma " + str(5) +" lat")
print("{} ma {} lat".format(imie, 5))
print("{0} ma {1} lat".format(imie, 5))
wiek=5
print(f"{imie} ma {wiek} lat")

#listy

lista=[]
lista=[1, 4, "Ala", 4.5, imie, [1,2]]
lista[0]
lista.append(3)
lista[0]=10
lista2=lista + lista
lista_nowa=list()

#słownik

slownik={}
slownik={"imie":"Marek",
"wiek":35}
slownik["imie"]
print(slownik.keys())
print(slownik.values())
print(slownik.items())

from marh import *
import math as m 

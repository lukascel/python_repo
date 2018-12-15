"""a = eval(input ("podaj dowolną wartość"))
b = eval(input ("podaj dowolną wartość"))
c = eval(input ("podaj dowolną wartość"))
d = eval(input ("podaj dowolną wartość"))
e = eval(input ("podaj dowolną wartość"))

#EVAL pozwala wpisywać wszystko jako int

lista = []

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
#print(lista)

lista_nowa = []

for elem in lista:
    if type(elem) == str:
        lista_nowa.append(elem)
print (lista_nowa)"""

"""słowniki para - klucz - wartość
metody:
keys, - zwraca klucze
values, - zwraca wartości
itoms, - zwraca krotki

klucz musi byc niezmienny - tupla.
"""
#P39
"""slownik = {
    "jeden":1,
    "dwa":2,
    "trzy":3,
    "cztery":4,
    "pięć":5
}

a = input("podaj wartość")
print (slownik[a])
"""

#P41
"""kod = input("podaj kod produktu")
ilosc = int(input("podaj ilość produktu"))

produkty = {
    "k1" : ("nazwaK1", 10.0),
    "k2" : ("nazwaK2", 12.0),
    "k3" : ("nazwaK3", 100.0)
}
#print (produkty[kod])
#print (produkty [kod][0])
#print (produkty [kod][1])

print ("zamówienie:", (produkty[kod][1] * ilosc), produkty [kod][0])
"""
#OPERACJE NA ZBIORACH
"""a = [1,2,3]
b = (4,5,6)

a_set = set(a)
b_set = set(b)

print (a_set | b_set)
print (a_set & b_set)
print (a_set - b_set)
print (b_set - a_set) # różnica symetryczna
"""
#P42
""" pierwsze - nie mam gwarancji, że się nie zrobi duplikat:
from random import randint
print (randint(1, 49))
"""
#lub:
"""from random import randint
lotto = set ()

while(len(lotto) < 6):
    lotto.add(randint(1, 49))
print (lotto)
"""
#P43
"""x = list(range(0,21,2))
y = list(range(0,11,1))

xy = (x, y)
print (xy)
print (xy [0][0], xy [1] [0])
print (xy [0] [1], xy [1][1])
"""

#LUB TAK:
#y=1/2x
"""lista=[]
count = 0

while count <11:
    a = (count*2,count)
    lista.append(a)
    count=count+1
print(lista)
"""

#P44
"""
a = input ("podaj wartość")
b = input ("podaj wartość")
c = input ("podaj wartość")
d = input ("podaj wartość")
e = input ("podaj wartość")

lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
print (lista)
set_lista = set(lista)

print (set_lista) # bo jak użyję zbioru to usunie mi duplikaty, cokolwiek by mi ktoś nie wpisał.

print (len(set_lista))
"""
#lub tak:
"""x= input ("podaj wartość")
mojSet = set()

while x != "exit":
    mojSet.add(x)
    x = input("podaj wartość")
print(len(mojSet))
"""
""" a teraz modyfikacja - jeśli wpisze exit lub coś się powtórzy to zamknij program"""
"""
x= input ("podaj wartość")
mojSet = set()

while x != "out":
    if x in mojSet:
        exit()
    mojSet.add(x)
    x = input("podaj wartość") #po zrobieniu seta z powyższej linijki dodaj nową wartość
print(len(mojSet))
"""
# INSTRUKCJE WARUNKOWE: wyświetla pierwszy spełniony warunek
"""
if 1<2:
    print ("1<2")
elif 1<3:
    print ("1<3")
else:
    pass
"""
#trójargumentowy - prosty ale narazie dla powtórzenia trzeba normalnego ifa stosować.
"""
a = 25
b = 30

print(b) if (a<b) else print (b)
"""
#P45
"""
test = list(range(0,5))
if (bool(test[0])):
    print (test[0])

if (bool(test[1])):
    print (test[1])

if (bool(test[2])):
    print (test[2])

if (bool(test[3])):
    print (test[3])

if (bool(test[4])):
    print (test[4])
"""
#P46
"""
a = int(input("podaj wartość"))

if (a) => 0 and (a) <10:
    print ("in range")
else:
    print ("out of range")
"""
#lub: - łatwiejszy sposób w materiałach na trello.

#P47
"""lista = [3,0,3,4,4]

if (lista[0] > 0) and (lista[1] >= 0):
    print ("++")
elif (lista[0] > 0) and (lista[1] <= 0):
    print('++')
elif (lista[0] <= 0) and (lista[1] > 0):
    print('+-')
else:
    print('--')
"""
#P48 - błąd jakiś...?
"""
a = int(input("podaj liczbę")%2)
dict = {
    "parzysta":       a%2==0,
    "nieparzysta":    a%2!=0}

print (dict(a))
"""

#P49
#USER : USER
#ADMIN : ADMIN
#Pkolejne - jakiś błąd - zły mam wynik
"""
access_dict = {
    "user" : "user",
    "admin" : "admin"
}

login = input ("podaj login")
password = input ("podaj haslo")

if login in access_dict and password == access_dict[login]: #login jest kluczem, sprawdza czy po tym zgadza się kolejna wartość
    print ("zalogowany")
    if login == "admin":
        print ("panel admina")
    else:
        print ("panel użytkownika")
else:
    print ("nieprawidłowe dane")
"""
#funkcja CONTINUE - przechodzi do kolejnej iteracji!!
#funkcja ENUMERATE
"""
a = [1,2,3,4,5]

for index, value in enumerate(a):
    print (index, value)

zmienna = enumerate(a)
print (list(zmienna))
"""

#FORMATOWANIE Dlugosci wyjscia (slajd 43)
"""
for x in range (5,100,10):
    print ("%12i%12i%12i" % (x, x**2, x**3))
"""
"""
for x in range(5, 100, 10):
    print("pierwiastkiem liczby %10i jest %5.1f" % (x, x**0.5)) # i - odległości, f - ilosc miejsc po porzecinku
"""
"""
for x in range(5, 100, 10):
    print ("%3i%#6o%#5x" % (x,x,x)) # na podstawie slajdu 43 - rekoduje system dziesiętny na ósemkowy i szesnastkowy
"""
"""
for x in range(5, 100, 10):
    print ("%-3i%#-6o%#-5x" % (x,x,x)) # - powoduje wyrównanie odwrotne
"""
"""
for x in range(5, 100, 10):
    print ("%3i%#044o%#04x" % (x,x,x)) # zastąpienie spacji zerami.
"""
"""
#wypisanie ciągu tekstowego ze zmiennych:
a = 24
b = "sample"
c = 27
d = "text"

print (str(a) + b + str(c) + d)
#lub
print ("%4i %s %i %s" % (a,b,c,d))
"""
"""Przykład z prezentacji - s.48 ale w prezentacji jest błąd
liczby = [eval(input("Podaj liczbę:")),
          eval(input("Podaj liczbę:")),
          eval(input("Podaj liczbę:"))]

szukana = eval(input("Podaj liczbę do znalezienia:"))

for p,x in enumerate(liczby):
    if x != szukana:
        continue
    print("Znaleziono liczbę %i na pozycji %i" % (x,p+1))
    break
else:
    print("Liczby %i nie ma na liście" % szukana)
"""
#P51
"""
a = input("podaj ciąg cyfr")

dict = {
    0:"zero",
    1:"jeden",
    2:"dwa",
    3:"trzy",
    4:"cztery",
    5:"pięć",
    6:"sześć",
    7:"siedem",
    8:"osiem",
    9:"dziewięć"
}
result = ""

for znak in a:
    if (znak.isdigit()):
        result += dict[int(znak)]
        result += ' '
    else:
        result += "x"
print (result)
"""

#P53
"""
a = list(range(3,10))
print (a)

for elem in a:
    print (elem, elem**2)
"""
#można dodać formatowanie zgodne z S43(?) - sprawdzić z zadaniem Marcina z Trello - inny sposób

#P54
"""numbers = [5,2,1,10]
print (numbers.index(int(input("podaj number"))))
"""

#P55
#podpowiedź: celsius *1.8 = fahrenheit -32
#celsius = (fahrenheit -32)/1.8
"""
celc = range (45,-21,-5)
for x in celc:
    y = 32+x*1.8
    print ("%+5i st.C = %+5i st.F" % (x,y))
"""

############################
#ZADANIE do domu P50
############################

#tabliczka mnożenia 10x10

for x in range (1,11):
    for y in range (1,11):
        print (x*y,)
    print ("\n")
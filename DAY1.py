

a = 1
print (type(a))

a = "sample text"
print (type(a))

a= 1.0
print (type(a))

pi = 3.14
print (type(pi))

myChar = 'a'
print (type(myChar))

imie = "Anna"

adreszamieszkania = "Nieznana 20"

#adres-zamieszkania = "Nieznana 20" - bo myślnik

drugie_imię= "Beata"

#3ulubionePotrawy = "x, y, z"

#and = 51
and_Dana = 1023

#And = "hello" - nie zaczynamy od duzej

#twoje zainteresowania = "nurkowanie" - spacja w nazwie

twoje2samochody = "v, m"

śćółżęąćł= ":-)"

twojaSzczesliwaLiczbaKtoraWylosowanoSpecjalnieDlaCiebie= 5

# komentarz jednolinijkowy
""" komentarz wielolinijkowy - wszystko co w nim zamknięte"""

c = 45
print(c)

d = "szkolenia"
print(d)

e = 23.5
print(e)

f = "Test"
print(f)

g = '?'
print(g)
print (c, d, e, f, g)

###############################
# SYNTAX
###############################


############################
#Tuple - "krotka"
############################
a = (1, 2, 3)
print (type(a))

print (a[0])
print (a[1])
print (a[2])

a = (1, 2, 3, 's', 'a', 'm', 'p')
print (type(a))

print (a[4])

#utworzenie jednoelementowej krotki - za pomocą przecinka
a = (1,)
print (type(a))

#Tuple is IMMUTABLE!!!! krotka jest niemodyfikowalna! ponizsze poelcenie da błąd
#a[0] = 4
#drugi sposób na krotkę:
a = 1, 2, 3, 4, 's', 'a', 'm', 'p'
print (type(a))

#trzeci sposób na krotkę - funkcja:
a = tuple((1,2,3))
print (type(a))

############################
# List
############################
a = [1, 2, 3, 4, 5, 's', 'a', 'b', 'c']
print (type(a))
print (a[5])

a[2] = "nowa"
print (a)

#dodawanie do listy:
a.append('nowa2')
print (a)

#dodawanie do listy na miejscu drugim:
a.insert (2, "nowa3")
print (a)

#usuwanie z listy na miejscu konkretnym - tutaj na zerowym:
del a[0]
print (a)

#sprawdzenie wielkości listy
print (len(a))

#krotka z listy - i już tej listy nie bede mógł modyfikować:
a_tuple = tuple(a)
print (type(a_tuple))


##ZADANIE - napisz "program" żeby dla zdefiniowanych zmiennych zamienił wynmiki
a = 1
b = 2

c = a
a = b
b = c

print(a) #2
print(b) #1
# ale w pythonie można łatwiej:
a = 1
b = 2
a,b = b,a
######koniec zadania


# wyświetlanie elementów listy - po koleii każdy element!! Za elem mogę podstawić cokolwiek - to tylko nazwa zmiennej
#UWAGA  - to jest pętla! musi być wcięcie w pętli!

a = [1, 2, 3, 4, 5, 's', 'a', 'b', 'c']

#for each:
for elem in a:
        print (elem)
## wypisuje wszystkie wartości z zadanego przedziału, z krokiem na ostatnim miejscu (1)
# wynik jest bez ostatniego elementu listy - bo z tej strony nawias jest otwarty.
a = list (range (1,6,1))
print (a)

#mogę zrobić pętlę 5 razy liste a:
#aby zrobić coś kilka razy w petli - muszę za pomocą dodatkowej listy!!!!
for elem in a:
    print (elem)

#Wypisanie pierwszych pięciu elementów z listy. Więc potrzebuje zrobić pięć razy pętlę
#counter +=1 pozwala zliczać

a = list (range (1,6,1)) #< ) - zbiór jest zamknięty z prawej strony
print(a)
my_list = [1, 2, 'log', 3, 4, 5, 's', 'a', 'b', 'c']
counter = 0
for elem in a:
    print (my_list[counter])
    counter +=1 #counter = counter + 1

#a po tupli? Można - wywołaj każdy element tupli
my_tuple =('a', 'b', 'c')
for elem in my_tuple:
    print (elem)
#wywołaj dwa elementy z mojej tupli
a = list(range(1,3,1)) #< )
# da wynik: [1, 2]
print (a)
counter = 0
for elem in a:
    print (my_tuple[counter])
    counter +=1

a = [1, 2, 3, 4, 5]
for elem in a:
    print (elem*2)

a = ['a', 'b', 'c']
for elem in a:
    print (elem*2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #to samo ponizej:
a = list(range(1, 11,1))

new_list = []
new_list2 = []
for elem in a: #to należy czytać: przejdź przez każdy element,
    # jeśli >3 to nowa lista
    if elem > 3:
        new_list.append(elem)
    else:
        new_list2.append(elem)
print (new_list) #ten print jest już poza forem - to widać po wcięciach!
print (new_list2)

##### lista która zawiera liczby parzyste wśród 1-10
a = list(range(1, 11, 1))
lista_parzyste = []
for elem in a:
    if elem %2 == 0: # ==0 oznacza że wartość z dzielenia (%2) jest 0
        lista_parzyste.append(elem)
print (lista_parzyste)

a = "sample text"
for letter in a:
    print (letter)


counter = 0
while counter<5: #dopóki warunek jest prawdziwy - pętla sie wykonuje
    print (counter)
    counter +=1 # counter = counter +1
# WHILE stosuje kiedy nie wiem ile razy pętla ma się zrobić. Póki warunek jest spełniony
# FOR - zakładam ile razy pójdzie.

"""
while 1==1: 
counter = 4
    if counter < 0:
        break
        counter =- 1 #counter = counter -1

if 1<2:
    pass"""

################################
#Set - zbiór -
    # nie ma duplikujących sie danych!
    # nie da sie indeksować
    # jest nieuporządkowany
    # moża utworzyć poprzez wypisanie elementów w klamrowym nawiasie:
    #a = {1,2,3,4}
################################
a = [1,1,1,1,2,3,4,5,6]
b = "sample text"
c = (1,2,1,2,3)

a_set = set(a)
print(type(a_set))

b_set = set(b)
print(type(b_set))

c_set = set(c)
print(type(c_set))

print(a_set)

print(b_set)

print(c_set)
#Sprawdź, czy w zbiorze a istnieje jedynka:
for elem in a_set:
    if elem ==1:
        print ("ok, istnieje")
#lub łatwiej:
print (1 in a)

a = {1,2,3}
#dodawanie elemetów
a.add(4)
print(a)

#usuwanie elementu ze zbioru: remove - nie del, bo del wymaga podania miejsca z którego usuwa a w zbiorze nie mogę!
a.remove(1)
print (a)

a = [1,2,3]

#frozenset is immutable - niemodyfikowalny zbiór!
a_set = frozenset(a)

#########################
#TABLICE ASOCJACYJNE
#########################
# wprowadzenie - awaria koputera

#funkcja zwracajaca krotki złożone z klucza i wartości
"""numbers = {
    'a' : 2,
    'b': 3,
    'c': 4
}

print (numbers.items())
items = numbers.items()
for item in items:
    print (itemprint item[0])
    print (item [1])
## powyzej bledy od awarii komputera
"""


#SLIICES - proste przykłady
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:3:1])
print(a[0:7:2])
print(a[len(a) -1]) # pokaż ostatni element
print(a[-1]) # ostatni element
print(a[-1:-4:-1])
print(a[::]) #- od poczatku do końca
print(a[::-1])  #wszystko wstecznie

# SKLADNIA

text = "sample text" #wyciągnij z tego dwa słowa
textList = text.split(" ") #wskazuje co jest separatorem
print(textList) #efekt: ['sample', 'text']

print("_".join(textList)) # z powyższego połącz w jedno używajac separatora który jest w " " tej metody

a = "sample text" # - zapisz od tyłu
print(a[::-1])

##ZADANIE P0c

zmienna_1 = "Ciekawe"
zmienna_2 = "Programowanie"
zmienna_3 = "Jest"
zmienna_4 = "Wciągające"
zmienna_5 = "I"

zdanie = zmienna_2 + " " + zmienna_3 + " " + zmienna_1 + " " + zmienna_5 + " " + zmienna_4 + " "
print(zdanie)

#ZADANIE P10

brutto = 1000
VAT1 = 0.03
VAT2 = 0.07
VAT3 = 0.23

suma1 = brutto * VAT1
suma2 = brutto * VAT2
suma3 = brutto * VAT3

netto1 = brutto - suma1
netto2 = brutto - suma2
netto3 = brutto - suma3


print(round(netto1,2))
print(round(netto2,2))
print(round(netto3,2))

######P11:
chleb = 1.99
mleko = 2.5
cukierki = 12.99

zakupy = 2*chleb + 0.5*mleko + 0.3*cukierki
print(round(zakupy,2))

####### systemy liczbowe

a = 0o11
print(a)
a = 0o27
print(a)
#wynik 23 bo 2*(8**1) + 7* (8**0) = 16 + 7.

#zmienne logiczne - w pythonie wszystko co jest czymś jest true a nic - fals.
#P17
print(bool(7))

#P22
a = " Adam"
b = "Kowalski"
c = "wiek: 35 lat"
d = "pensja: 6000"
e = "młodszy inżynier procesu"

print (10*(a + " " + b + ", " + c + ", " + d +", " + e ))
### niby ok ale to jest hardcodowane, trzeba użyć łączenia stringa z integerem! - zweryfikować!

#proste polecenie:

a=257
b=257

print (a is b)
print (id(a))
print (id(b))

#ZADANIE P22a

dochod1 = 700
koszty = 500
zysk1 = 200

dochod2 = 1.5 * dochod1
zysk2 = dochod2 - koszty
print(round(zysk2,2))

dochod3 = 1.5 * dochod2
zysk3 = dochod3 - koszty
print(round(zysk3,2))

dochod4 = 1.5 * dochod3
zysk4 = dochod4 - koszty
print(round(zysk4,2))

dochod5 = 1.5 * dochod4
zysk5 = dochod5 - koszty
print(round(zysk5,2))

dochod6 = 1.5 * dochod5
zysk6 = dochod6 - koszty
print(round(zysk6,2))

#OPERATORY
#p25
netto = 5500
brutto = 1.23 * netto
stawka = brutto/168
print(round(stawka,2))

#OPERATORY
print (1 and 2) # jesli jest prawda to zwraca ostatnia wartośc, fałsz - zwraca pierwszy fałsz

#P27
a = bool(0)
b = bool(0)
c = bool(1)

W1 = not(a) and not(b) and not(c)
W2 = not(a) and not(b) and c
W3 = not(a) and b and not(c)
W4 = a and not(b) and not(c)

W = W1 or W2 or W3 or W4
print (W)

#OPERATORY RELACJI
#P29
"""imie = input("wpisz coś")
print (30 * (imie + "\n"))
"""
#P30
"""h = int(input("podaj wysokość:"))
a = int(input("podaj dl podstawy"))
print((1/2)*a*h)
"""
### TYPY SEKWENCYJNE

####### ZADANIA DODATKOWE
a = "aaaaabbbccc"
dictionary = dict{}

for letter in a:
    if letter in dictionary:
        dictionary[letter] +=1
    else:
        dictionary[letter] = 1
print(dictionary)

"""zakladanie słownika:
a = dict()
print (type(a))
.
.
."""


#można to robić printami a.count:
print(a.count('a'))
print(a.count('b'))
print(a.count('c'))


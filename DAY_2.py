a = eval(input ("podaj dowolną wartość"))
b = eval(input ("podaj dowolną wartość"))
c = eval(input ("podaj dowolną wartość"))
d = eval(input ("podaj dowolną wartość"))
e = eval(input ("podaj dowolną wartość"))

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
print (lista_nowa)
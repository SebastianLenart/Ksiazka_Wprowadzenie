"""
Jeśli X jest obiektem iterowanym, wywołanie
next(X) da ten sam efekt co wywołanie X.__next__(), jednak kod jest o wiele bardziej estetyczny. W przypadku plików możemy stosować dowolną z form:

f = open('script1.py')
f.__next__() # Bezpośrednie wywołanie metody iteratora
'import sys\n'
f.__next__()
'print(sys.path)\n'
f = open('script1.py')
next(f) # Niejawne wywołanie metody __next__
'import sys\n'
next(f)
'print(sys.path)\n'`
# ------------------ ITER ----------------------------------
 W przypadku plikow nie ma potrzeby robienia ITER(..)
L = [1, 2, 3]
I = iter(L) # Pozyskanie obiektu iteratora
I.next() # Odczyt następnego elementu iteratora
1
I.next()
2
I.next()
3
I.next()
# ------------------ Jawnie i Niejawnie ----------------------------------
L = [1, 2, 3]
for X in L: # Iteracja automatyczna
... print(X ** 2, end=' ') # Wywołuje funkcję iter(), metodę __next__(), przechwytuje wyjątki
...
1 4 9

I = iter(L) # Ręczna iteracja: pętla for robi to samo niejawnie
while True:
... try: # Instrukcja try pozwala obsługiwać wyjątki
... X = next(I) # Alternatywnie: I.__next__()
... except StopIteration:
... break
... print(X ** 2, end=' ')
...
1 4 9
#-------------------- ENUMARATE -----------------------------
E = enumerate('spam') # Wynik funkcji enumerate() również jest obiektem iterowanym
E
<enumerate object at 0x0253F508>
I = iter(E)
next(I) # Wygenerowanie wyników z użyciem protokołu iteracyjnego
(0, 's')
next(I) # Przekształcenie na listę generuje wszystkie elementy jednocześnie
(1, 'p')
list(enumerate('spam'))
[(0, 's'), (1, 'p'), (2, 'a'), (3, 'm')]
Z reguły nie mamy okazji obserwować tych szczegółów w działaniu, ale są one wykorzystywane
niejawnie przez mechanizm pętli for. W rzeczywistości wszelkie przypadki kolejnego przeglądania elementów w Pythonie wykorzystują protokół iteracyjny. Kolejne przykłady poznamy
w następnym punkcie


"""
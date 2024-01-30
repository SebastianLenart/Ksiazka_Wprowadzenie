"""
for <cel> in <obiekt>: # Przypisanie elementów obiektu do celu
 <instrukcje>
 if <test>: break # Wyjście z pętli, pominięcie else
 if <test>: continue # Przejście na górę pętli
else:
 <instrukcje> # Jeśli nie trafiliśmy na break


 #-------- przyklad ------
 for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
...
1 2 3
4 5 6

# -------- inny dziwniejszy przyklad -----
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)
...
1 2 3
X Y 6


#------ ekstracja z * ------------------------------------------
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
... print(a, b, c)
...
1 [2, 3] 4
5 [6, 7] 8








"""
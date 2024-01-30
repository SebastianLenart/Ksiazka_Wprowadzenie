"""
# modyfikacja listy:
L = [1, 2, 3, 4, 5]
for x in L:
... x += 1
...
L
[1, 2, 3, 4, 5]
x
6

jak widac na gorze nie dziaa, ale ponizszy kod bedzie dziaac:
L = [1, 2, 3, 4, 5]
for i in range(len(L)): # Dodanie 1 do każdego elementu listy L
... L[i] += 1 # Lub L[i] = L[i] + 1
...
L
[2, 3, 4, 5, 6]

Nie da się uzyskać tego
samego za pomocą prostej pętli w stylu for x in L:, ponieważ taka pętla przechodzi same
elementy listy, a nie ich pozycje




# ----- ZIP ------
By połączyć elementy z tych dwóch list, możemy wykorzystać funkcję zip do utworzenia listy
par krotek.

zip(L1,L2) # moze byc wiecej L3, L4..
<zip object at 0x026523C8>
list(zip(L1, L2)) # list() wymagane w Pythonie 3.0, w 2.6 nie
[(1, 5), (2, 6), (3, 7), (4, 8)]
-----
 for (x, y) in zip(L1, L2):
... print(x, y, '--', x+y)
...
1 5 -- 6
2 6 -- 8
3 7 -- 10
4 8 -- 12
------ ZIP rozna dlugosc ---------
Co więcej, kiedy długość argumentów różni się, funkcja zip odcina wynikowe krotki do długości najkrótszej sekwencji.
W poniższym przykładzie łączymy ze sobą dwa łańcuchy w celu
równoległego wybrania znaków, jednak wynik składa się jedynie z tylu krotek, jaką długość ma
najkrótsza sekwencja:
S1 = 'abc'
S2 = 'xyz123'

list(zip(S1, S2))
[('a', 'x'), ('b', 'y'), ('c', 'z')]




"""
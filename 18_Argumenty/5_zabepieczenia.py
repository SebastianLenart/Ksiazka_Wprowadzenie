"""

Bez argumentów mogących być tylko słowami kluczowymi musimy użyć zarówno formy
*argumenty, jak i **argumenty i ręcznie badać słowa kluczowe, natomiast po wykorzystaniu
rozwiązania z argumentami mogącymi być tylko słowami kluczowymi wymagana jest mniejsza ilość kodu.
Poniższy kod gwarantuje, że żadne argumenty pozycyjne nie zostaną błędnie
dopasowane do notify, i wymaga, by przy przekazaniu było to słowo kluczowe:
def process(*args, notify=False): ...
-----------------------------------------------------------------------------------------------------------------
• Pierwsza funkcja pobiera pierwszy argument (args jest krotką) i przechodzi resztę, odcinając
pierwszy argument (nie ma sensu porównywać obiektu z samym sobą, w szczególności
jeśli może on być większą strukturą).
• Druga wersja pozwala Pythonowi na automatyczne wybranie pierwszego i pozostałych
argumentów, zatem unika indeksowania i wycinka.
• Trzecia metoda dokonuje konwersji krotki na listę za pomocą wywołania wbudowanej
funkcji list i stosuje metodę listy sort

def min1(*args):
 res = args[0]
 for arg in args[1:]:
 if arg < res:
 res = arg
 return res
def min2(first, *rest):
 for arg in rest:
 if arg < first:
 first = arg
 return first
def min3(*args):
 tmp = list(args) # Lub w Pythonie 2.4+: return sorted(args)[0]
 tmp.sort()
 return tmp[0]
print(min1(3,4,1,2))
print(min2("bb", "aa"))
print(min3([2,2], [1,1], [3,3]))

Warto zauważyć, że żaden z trzech wariantów nie sprawdza przypadku, w którym nie przekazano żadnych argumentów.
Mogłyby to robić, ale nie ma to tutaj sensu — we wszystkich
trzech rozwiązaniach Python automatycznie zgłasza wyjątek, jeśli do funkcji nie przekazano
żadnych argumentów. Pierwszy wariant zwraca wyjątek, kiedy próbujemy pobrać element
zerowy, drugi — kiedy Python wykrywa niedopasowanie listy argumentów, natomiast trzeci —
kiedy próbujemy na końcu zwrócić element zerowy
---- inny przyklad ----------------------------------------------------------------------------------------------------
def intersect(*args):
 res = []
 for x in args[0]: # Przejrzenie pierwszej sekwencji
 for other in args[1:]: # Dla wszystkich pozostałych argumentów
 if x not in other: break # Element w każdym z nich?
 else: # Nie — wyjście z pętli
 res.append(x) # Tak — dodanie elementów na końcu
 return res
def union(*args):
 res = []
 for seq in args: # Dla wszystkich argumentów
 for x in seq: # Dla wszystkich węzłów
 if not x in res:
 res.append(x) # Dodanie nowych elementów do wyniku
 return res
"""
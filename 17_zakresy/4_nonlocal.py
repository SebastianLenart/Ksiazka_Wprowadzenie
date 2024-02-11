"""
W przeciwieństwie do global instrukcja nonlocal ma zastosowanie do zmiennej
z zakresu funkcji zawierającej, a nie do zakresu modułu poza wszystkimi instrukcjami def. I inaczej niż w global —
w przypadku nonlocal zmienne muszą w momencie deklaracji istnieć
już w zakresie funkcji zawierającej — mogą istnieć jedynie w funkcjach zawierających i nie
mogą być tworzone za pomocą pierwszego przypisania w zagnieżdżonej instrukcji def

Innymi słowy, instrukcja nonlocal zarówno pozwala na przypisywanie do zmiennych w zakresach funkcji zawierającej,
jak i ogranicza przeszukiwanie zakresów dla zmiennych tego typu
jedynie do instrukcji def zawierających funkcję


def tester(start):
... state = start # Referencja do zmiennej nielokalnej działa normalnie
... def nested(label):
Instrukcja nonlocal | 457
... print(label, state) # Pamięta stan w zakresie funkcji zawierającej
... return nested
...
F = tester(0)
F('mielonka')
mielonka 0
F('szynka')
szynka 0
Modyfikacja zmiennej w zakresie instrukcji def funkcji zawierającej nie jest jednak domyślnie
dozwolona — tak samo jest również w wersji 2.6:
def tester(start):
... state = start
... def nested(label):
... print(label, state)
... state += 1 # Domyślnie nie może się zmienić (w 2.6 też nie)
... return nested
...
F = tester(0)
F('mielonka')
UnboundLocalError: local variable 'state' referenced before assignment
#----------------------------------------------------------------------------------------------------------
def tester(start):
... state = start # Każde wywołanie otrzymuje własną zmienną state
... def nested(label):
... nonlocal state # Pamięta state z zakresu funkcji zawierającej
... print(label, state)
... state += 1 # Można zmienić, jeśli nonlocal
... return nested
...
F = tester(0)
F('mielonka') # Inkrementuje state z każdym wywołaniem
mielonka 0
F('szynka')
szynka 1
F('jajka')
jajka 2
#----------------------------------------------------------------------------------------------------------
def tester(start):
... def nested(label):
... nonlocal state # Zmienne nielokalne muszą już istnieć w zakresie funkcji zawierającej!
... state = 0
... print(label, state)
... return nested
...
SyntaxError: no binding for nonlocal 'state' found
#----------------------------------------------------------------------------------------------------------
spam = 99
def tester():
... def nested():
... nonlocal spam # Musi być w instrukcji def, nie w module!
... print('Aktualna wartość=', spam)
... spam += 1
... return nested
...
SyntaxError: no binding for nonlocal 'spam' found










"""
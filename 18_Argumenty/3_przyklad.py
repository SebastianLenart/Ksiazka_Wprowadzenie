"""


!!!
Ponownie nie należy mylić składni z * oraz ** w nagłówku funkcji i jej wywołaniu. W nagłówku
służy do zebrania dowolnej liczby argumentów, natomiast w wywołaniu rozpakowuje dowolną
liczbę argumentów
!!!


def f(a, *pargs, **kargs): print(a, pargs, kargs)
...
f(1, 2, 3, x=1, y=2)
1 (2, 3) {'y': 2, 'x': 1}
------------------------------------------------------------------------------------------------------
W nowszych wersjach Pythona składni z * można również użyć przy wywoływaniu funkcji.
W tym kontekście jej znaczenie jest odwrotnością znaczenia z definicji funkcji — rozpakowuje
kolekcję argumentów, zamiast ją budować. Możemy na przykład przekazać do funkcji cztery
argumenty w krotce i pozwolić Pythonowi na rozpakowanie krotki na pojedyncze argumenty.
def func(a, b, c, d): print(a, b, c, d)
...
args = (1, 2)
args += (3, 4)
func(*args)
1 2 3 4
------------------------------------------------------------------------------------------------------
W podobny sposób składnia z ** w wywołaniu funkcji rozpakowuje słownik par klucz-wartość
na pojedyncze argumenty ze słowami kluczowymi.
args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)
1 2 3 4
------------------------------------------------------------------------------------------------------
I znów w wywołaniu możemy na wiele elastycznych sposobów połączyć normalne argumenty
pozycyjne oraz argumenty ze słowami kluczowymi.
func(*(1, 2), **{'d': 4, 'c': 4})
1 2 4 4
func(1, *(2, 3), **{'d': 4})
1 2 3 4
func(1, c=3, *(2,), **{'d': 4})
1 2 3 4
func(1, *(2, 3), d=4)
1 2 3 4
f(1, *(2,), c=3, **{'d':4})
1 2 3 4



"""
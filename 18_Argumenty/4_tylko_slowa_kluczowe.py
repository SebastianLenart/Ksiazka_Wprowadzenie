"""
W Pythonie 3.0 uogólniono reguły kolejności w nagłówkach funkcji w taki sposób, by możliwe
było podawanie argumentów mogących być tylko słowami kluczowymi (ang. keyword-only argument) —
czyli argumentów, które trzeba przekazywać za pomocą słowa kluczowego i które
nigdy nie zostaną wypełnione przez jakikolwiek argument pozycyjny. Jest to przydatne, jeśli
chcemy, by funkcja zarówno przetwarzała dowolną liczbę argumentów, jak i przyjmowała
możliwie opcjonalne opcje konfiguracyjne

def kwonly(a, *, b, c):
... print(a, b, c)
...
kwonly(1, c=3, b=2)
1 2 3
kwonly(c=3, b=2, a=1)
1 2 3
kwonly(1, 2, 3)
TypeError: kwonly() takes exactly 1 positional argument (3 given)
kwonly(1)
TypeError: kwonly() needs keyword-only argument b
---------------------------------------------------------------------------------------------------------
Poniżej znajduje się odpowiednik
wersji z argumentami mogącymi być tylko słowami kluczowymi:
# Zastosowanie usunięcia argumentów-słów kluczowych z wartościami domyślnymi
def print30(*args, **kargs):
 sep = kargs.pop('sep', ' ')
 end = kargs.pop('end', '\n')
 file = kargs.pop('file', sys.stdout)
 if kargs: raise TypeError('dodatkowe słowa kluczowe: %s' % kargs)
 output = ''
 first = True
 for arg in args:
 output += ('' if first else sep) + str(arg)
 first = False
 file.write(output + end)


"""
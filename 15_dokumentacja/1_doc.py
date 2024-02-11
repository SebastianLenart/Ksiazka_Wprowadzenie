"""

import sys
print(sys.__doc__)
This module provides access to some objects used or maintained by the interpreter and
´to functions that interact strongly with the interpreter.
Dynamic objects:
argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules
...resztę tekstu pominięto...
Opisy funkcji, klas oraz metod wbudowanych modułów również dołączane są za pomocą
atrybutów __doc__.
print(sys.getrefcount.__doc__)
getrefcount(object) -> integer
Return the reference count of object. The count returned is generally one higher than
you might expect, because it includes the (temporary) ...resztę tekstu pominięto...
Łańcuchy znaków udostępniają również więcej informacji na temat wbudowanych funkcji.
print(int.__doc__)
int(x[, base]) -> integer
Convert a string or number to an integer, if possible. A floating point argument will
´be truncated towards zero (this does not include a ...resztę tekstu pominięto...
print(map.__doc__)
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments from each of the
iterables. Stops when the shortest iterable is exhausted.


"""
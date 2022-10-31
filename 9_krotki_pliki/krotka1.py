y = (40,) # pojedycza krotka
"""
list, tuple => konwersja

"""
# zamiast konwersji na list modyfkujemy krotke
T = (4, 5, 6)
T = (1,) + T[1:]
print(T) # (1, 5, 6)
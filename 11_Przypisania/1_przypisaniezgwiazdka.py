seq = [1, 2, 3, 4]
a, *b = seq
print(" a:", a,"\n", "*b:", b)
# lub za pomocna wycinków
a, b = seq[0], seq[1:] # to samo!
print(a, b)
*c, d = seq
print(c, d)
c, d = seq[:-1], seq[-1] # to samo!
print(c, d)

a, *b, c = "Seba"
print(a, b, c)

# !!!
# *a = "Seba" # blad, ponizej poprawna wersja
*a, = "Seba"
print()





text = '%s: %-.4f, %05d' % ('Wynik', 3.14159, 42)
print(text)
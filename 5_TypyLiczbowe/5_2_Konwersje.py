from typing import FrozenSet


from fractions import Fraction
print((2.5).as_integer_ratio()) # (5, 2)

f = 2.5
z = Fraction(*f.as_integer_ratio()) # * rozdziela krotke na pojedyncze argumenty
print(z) # 5/2
z.limit_denominator() # uproszczenie do najbliższego ulamka
print(z)

from pyads import *
print(0xA2) # szesnastkowo, 162
print(0o7) # osemkowo, 7
print(0b110) # binarnie, 6
print("-----------------------")
print(hex(123))
print(oct(123))
print(bin(123))
print("-----------------------")
print(int("123", 8)) # rzutowanie konwersja
print("-----------------------")
a = 1/3
b = 3
c = 0b0110
print(a.as_integer_ratio)
print(a.is_integer)
print(str(a),"typ", type(str(a)))
print(repr(a), "typ", type(repr(a)))
print("-----------------------")
print(c<<2,bin(c<<2)) # 8 + 16 = 24
print(c>>1) # 2 + 1 = 3
print("-----------------------")
print(11//5)
print(11/5)
print("-----------------------")
x = 0b001100
print(bin(x|0b101010))
print(bin(x&0b101010))
print(bin(x^0b101010))
print("-----------------------")
x=9
print(bin(x)," dlugosc: ", x.bit_length())
print("-----------------------")

#globalne ustawienie precyzji
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 3
print(decimal.Decimal(1) / decimal.Decimal(7))
print(decimal.Decimal(str(1234)))
print("-----------------------")
# Typ liczby ulamkowej, operacje na ulamkach
from fractions import Fraction
xf = Fraction(2,3)
xg =Fraction(3, 4)
print(xf) # 2/3s
xSuma = xf + xg
print(xSuma)

print(Fraction('.25') + Fraction("1.25")) # 3/2
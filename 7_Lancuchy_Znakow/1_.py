"""
\n \t itd...
aby to wylaczzyc bo np. czytamy plik "C:\nowy\tekst.txt" ...
trzeba poprzedziec r np. r"C:\nowy\tekst.txt"
lub zastosowac zamiast \ to \\


"""
a = "Seba" + "stian"
print(a)
print("-"*20)
print(a[::2])
print(a[::-1])
print("-"*20)
S = "mielonka"
# S[0] = "x" blad, nie mozna modyfikowac, trze za pomoca replace
ss = "Ten %d %s jest martwy!" % (1,"ptak") #  d s jest tabela str 223 z tymi symbolami przed %
print(ss)
li = "%f, %.2f, %.*f" % (1/3.0, 1/3.0, 4, 1/3.0)
print(li)
#inaczej jeszcze
ss2 = "Ten {0} {1} jest martwy!".format(1, "ptak")
print(ss2)
ss3 = "Ten {} {} jest martwy!".format(1, "ptak")
print("ss3", ss3)

d = "{:,d} xx {:,d}".format(9999999, 7777777777)
print ("d", d)


dd = "{:,.2f}".format(296999.2567)
print(dd)

f = "%f, %.2f %06.2f" % (3.14159, 3.14159, 3.14159)
print(f)

""""
Typy niezmienne - liczby, lancuchy znakow, krotki, zamrozone zbiory
Typy zmienne - listy, slowniki, zbiory, bytearray

find podobne do in

"""
ileznakow = "a\nb\x1f\0000\d" # 8 znakow
print(len(ileznakow))



























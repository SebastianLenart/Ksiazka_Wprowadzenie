"""
wycinki nie dzialaja bo sanieuporzadkowane, losowe

przyklady:
D = {"mielonka" : 2}
D = dict(zip(keylist, valslist))
D = dict.fromkeys(["a","b"])
D.keys(), D.values(), D.items(), D.copy(),
D.get(key, default)
D.update(D2)
D.pop(key)
len(D)
D[key] = 42
del D[key]
list(D.keys())
D1.keys() & D2.keys()
D = {x: X** for x in range(10)}
has_key => powyzej3.0 nie dostepne

for key in D == for key in D.keys()

kluczem moze byc krotka ect... ale nie lista, bo lista jest modyfikalna

do nieistaniejacego klucza mozna sie odwolac przez get, lub try exept


"""
D = {"mielonka" : 2}
D1 = dict.fromkeys(["a", "b"] , 12) # domyslne wartosci wszystkich kluczy 
print(D1)



"""
L = []
L[99] = "mielonka"
# blad wywali

D = {}
D[99] = "mielonka"
D[99]..
# GIT

"""

D3 = {"a": 1, "b":2}
print("sorted", sorted(D3.items()))
print("list", list(D3.items()))









print([["lista "]*4])
print([1, 2] + list("34"))

L = ["abc", "ABD", "aBe"]
print(L.sort(key=str.lower)) # cos nie dziala chyba
print(L) # teraz dzila, czemu ? str 246
print(sorted(L, key=str.lower))
print(sorted([x.lower() for x in L], reverse=True))

"""
potem pokaze ze sorted jest lepsze od sort

"""
print("-"*20)
L1 = ["mielonka", "jajka", "szynka"]
print(L1.index("jajka")) # 1 
L1.insert(1, "tost")
print("index:", L1)
L1.pop( 1) # moze usuwac po indeksie
print("pop:", L1)
L1.remove("jajka")
print("remove:", L1)

# inne usuwanie
L1 = ["mielonka", "jajka", "szynka"]
del L1[:2]
print("del:", L1)
















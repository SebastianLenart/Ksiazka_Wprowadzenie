#Typy w Pythonie sa powiazane z obiektami a nie ze zmiennymi
x = 43
x = "Seba"
x = 3.14
x = [1, 2, 3]
# zmienne zawsze sa wskaznikami do obiektow

# ! uwaga
L1 = [1, 2, 3]
L2 = L1 # oryginalne referecje
L1[0] = 222
print(L2) # tez sie zmienia

# kopiowanie
L2 = L1[:]
L1[0] = 444
print(L2) # juz sie nie zmienia
# lub copy
import copy
L2 = copy.copy(L1)
L2 = copy.deepcopy(L1)
print("copy", L2)

#------------------------------------------
"""
is - sprawedzamidentycznosc obiektow, 
kiedy obie zmienne odnosza sie do tego samego obiektu
"""
L = [1,2,3]
M = L
print(L is M) # True
#------------------------------------------
import sys
print(sys,sys.getrefcount(1))
#------------------------------------------
print("-")

















"""
porownanie 
== 
is => czy 2 obiekty sa tak naprawde jednym (jeden adres pamieci)

None - jest czyms a nie niczym, wbrew nazwy!!!


"""

L1 = [1, "a"]
L2 = [1, "a"]
print(L1==L2, L1 is L2) # True False

S1 = "mielonka" # krotki string
S2 = "mielonka" 
print("krotki napis",S1==S2, S1 is S2) # True True

S1 = "mielonka kvnvnrv v vurnvrenvornv" # dlugi string
S2 = "mielonka kvnvnrv v vurnvrenvornv" 
print("dlugi napis",S1==S2, S1 is S2) # True True, powinnobyc false wd ksiazki


L = ["Gral"]
L.append(L)
print("L:", L) # L: ['Gral', [...]] cykl w obiekcie (zamiast nieskonczonej petli)
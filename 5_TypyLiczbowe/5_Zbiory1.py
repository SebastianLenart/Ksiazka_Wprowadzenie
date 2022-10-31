"""
w zbiorach nie da sie przechowywac list i slownik, w przeciwienstwie do krotek

"""

s = set([1,2,3])
print(s.union([3, 4])) #dodanie
print(s.intersection((1,3,5))) # {1, 3}
print(s.issubset(range(-5,5))) # True
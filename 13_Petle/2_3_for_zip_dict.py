"""
Co jednak zrobić, kiedy program uzyskuje klucze i wartości słownika w postaci list w czasie
wykonywania, już po utworzeniu skryptu? Powiedzmy na przykład, że mamy poniższe listy
kluczy i wartości.
keys = ['mielonka', 'jajka', 'tost']
vals = [1, 3, 5]
Jedną z możliwości przekształcenia ich w słownik będzie zastosowanie na listach funkcji zip
i równoległe przejście ich za pomocą pętli for.
list(zip(keys, vals))
[('mielonka', 1), ('jajka', 3), ('tost', 5)]
D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v
...
D2
{'tost': 5, 'jajka': 3, 'mielonka': 1}

-----------------LUB KROCEJ-------------------------

keys = ['mielonka', 'jajka', 'tost']
vals = [1, 3, 5]
D3 = dict(zip(keys, vals))
D3
{'tost': 5, 'jajka': 3, 'mielonka': 1}






"""
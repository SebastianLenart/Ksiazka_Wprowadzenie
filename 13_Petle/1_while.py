"""
while <test1>:
 <instrukcje1>
 if <test2>: break # Wyjście z pętli, pominięcie reszty
 if <test3>: continue # Przejście do góry pętli, do testu1
else:
 <instrukcje2> # Wykonywane, jeśli nie trafiliśmy na break !!!!!!


W połączeniu z częścią pętli else instrukcja break może często wyeliminować konieczność
używania opcji (flag) statusu wyszukiwania z innych języków programowania. Poniższy fragment kodu ustala na
przykład, czy dodatnia liczba całkowita y jest liczbą pierwszą, wyszukując
czynniki większe od 1.
x = y // 2 # Dla jakiegoś y > 1 # patrz nizej czemu // a nie /
while x > 1:
 if y % x == 0: # Reszta
 print(y, 'ma czynnik', x)
 break # Pominięcie reszty
 x -= 1
else: # Normalne wyjście
 print(y, 'jest liczbą pierwszą')
Zamiast ustawiać opcję statusu, która ma być sprawdzana przy wyjściu z pętli, wystarczy
wstawić instrukcję break w miejsce, gdzie odnaleziony zostaje czynnik. W ten sposób część else
zakłada, że będzie wykonana tylko wtedy, jeśli żaden czynnik nie zostanie odnaleziony. Jeśli
nie trafimy na break, liczba jest liczbą pierwszą

Warto również zauważyć, że kod ten musi
w Pythonie 3.0 wykorzystywać operator // zamiast / z uwagi na przejście / na „prawdziwe dzielenie”
opisane w rozdziale 5. (początkowe dzielenie musi odciąć resztę, a nie
ją zachować!)


# ------------- inny przyklad --------------------------------
while x: # Wyjście, gdy x jest puste
 if match(x[0]):
 print('Ni')
 break # Wyjście, ominięcie else
 x = x[1:]
else:
 print('Nie znaleziono') # Tylko wtedy, gdy wyczerpano x




"""























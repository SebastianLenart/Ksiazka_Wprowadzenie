"""
def changer(a, b): # Do argumentów przypisano referencje do obiektów
... a = 2 # Zmiana wartości jedynie zmiennej lokalnej
... b[0] = 'mielonka' # Zmiana współdzielonego obiektu w miejscu
Podstawy przekazywania argumentów | 467
...
X = 1
L = [1, 2] # Wywołujący
changer(X, L) # Przekazanie obiektów niezmiennych i zmiennych
X, L # X bez zmian, L jest inne
------------------------------------------------------------------------------------------------
L = [1, 2]
changer(X, L[:]) # Przekazanie kopii, tak by 'L' się nie zmieniło
------------------------------------------------------------------------------------------------
Tak naprawdę, choć Python nie obsługuje czegoś, co niektóre języki programowania nazywają przekazywaniem 
argumentów z „wywołaniem przez referencję”, zazwyczaj możemy to
symulować, zwracając krotki i przypisując wyniki z powrotem do oryginalnych zmiennych
z kodu wywołującego.
def multiple(x, y):
... x = 2 # Modyfikacja jedynie zmiennych lokalnych
... y = [3, 4]
... return x, y # Zwrócenie nowych wartości w krotce
...
X = 1
L = [1, 2]
X, L = multiple(X, L) # Przypisanie wyników do zmiennych wywołującego
X, L
(2, [3, 4]
Wygląda to tak, jakby kod zwracał dwie wartości, jednak tak naprawdę zwraca jedną — krotkę
dwuelementową z pominiętymi opcjonalnymi nawiasami
------------------------------------------------------------------------------------------------
Nieznana liczba argumentów (rozpakowywanie) — przekazanie dowolnej liczby argumentów zgodnie
z pozycją lub słowem kluczowym
Kod wywołujący może również użyć składni z * do rozpakowania kolekcji argumentów
na pojedyncze, osobne argumenty. Jest to przeciwieństwo użycia * w nagłówku funkcji —
w nagłówku oznacza zebranie dowolnej liczby argumentów, natomiast w wywołaniu jest
to przekazanie dowolnej liczby argumentów
-----------------   WAZNE!!!   ------------------------------------------------------------
Składnia Lokalizacja Interpretacja
func(wartość) Wywołujący Normalny argument — dopasowanie po pozycji
func(nazwa=wartość) Wywołujący Słowo kluczowe — dopasowanie po nazwie
func(*sekwencja) Wywołujący Przekazanie wszystkich obiektów z sekwencji jako pojedynczych
argumentów pozycyjnych
func(**słownik) Wywołujący Przekazanie wszystkich par klucz-wartość ze słownika jako pojedynczych
argumentów-słów kluczowych
def func(nazwa) Funkcja Normalny argument — dopasowuje przekazane wartości po pozycji
lub nazwie
def func(nazwa=wartość) Funkcja Domyślna wartość argumentu wykorzystana, jeśli wartość nie została
przekazana w wywołaniu
def func(*nazwa) Funkcja Dopasowuje i zbiera pozostałe argumenty pozycyjne (w krotce)
def func(**nazwa) Funkcja Dopasowuje i zbiera pozostałe argumenty-słowa kluczowe (w słowniku)
def func(*argumenty, nazwa)
def func(*, nazwa=wartość)
Funkcja Argumenty, które w wywołaniu muszą być przekazane za pomocą słowa
kluczowego (Python 3.0
------------------------------------------------------------------------------------------------


"""
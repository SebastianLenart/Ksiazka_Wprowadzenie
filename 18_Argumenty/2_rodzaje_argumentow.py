"""
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
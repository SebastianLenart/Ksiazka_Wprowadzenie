"""
#----------------- W PLIKACH ---------------------------------
lines = [line.rstrip() for line in open('script1.py')]
lines
['import sys', 'print sys.path', 'x = 2', 'print 2 ** 33']

# ----------------- IF IN LIST_COMPREHENSION ---------------------------------
lines = [line.rstrip() for line in open('script1.py') if line[0] == 'p']
lines
['print sys.path', 'print 2 ** 33']
W powyższym kodzie instrukcja if sprawdza każdy wiersz wczytany z pliku, weryfikując, czy
jego pierwszym znakiem jest p. Jeśli tak nie jest, wiersz ten jest pomijany w liście wyników
zamiast tego :

res = []
for line in open('script1.py'):
... if line[0] == 'p':
... res.append(line.rstrip())
...
res
['print sys.path', 'print 2 ** 33']
#----------------------SLOWNIKI-----------------------------------------------
{ix: line for (ix, line) in enumerate(open('script1.py')) if line[0] == 'p'}
{1: 'print(sys.path)\n', 3: 'print(2 ** 33)\n'}

Należy pamiętać, że metoda keys() nie zwraca listy kluczy, więc tradycyjnie stosowany
w starszych wersjach sposób przeglądania słownika po posortowanej liście kluczy nie zadziała w 3.0.
W takim przypadku należy w pierwszej kolejności przekształcić wynik metody
keys() na listę i dopiero na niej wykonać funkcję sorted()


"""
"""
pickle - przechowywanie obiektu w pliku tekstowym bez konwersji na string, np.:

D = {"a": 2, "b": 2}
F = open("datafile.pkl", "wb") # wb zapis binarny
import pickle
pickle.dump(D, F) / lub odwrotnie:  E = pickle.load(F) przy "rb" podczas open
F.close
-----
.bin to moze byc obraz lub dzwiek
-----
shelve
struct "wb" => struct.pack(">i4sh", 7, "jajko", 8) lub przy "rb" struct.unpack....
flush, 
mozna otwierac pliki bajtowwe, czyli z rozszerzeniem .bin !!!
co to eval = sprawdz



""" 

myfile = open("myfile.txt", "w")
myfile.write('hej sebastian/n')
myfile.write("zeganj /n")
myfile.close()

myfile = open("myfile.txt")
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close()

print(open("myfile.txt").read()) # czyta wszystko naraz

for line in open("myfile.txt"):
    print(line, end="")

# str 282 tabela podsumuwujaca zmiennosc struktur danych























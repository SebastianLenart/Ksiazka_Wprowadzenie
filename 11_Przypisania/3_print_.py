import sys

text = '%s: %-.4f, %05d' % ('Wynik', 3.14159, 42)
print(text)

# ---------------------------------------
# print(x, y, z, sep='...', file=open('data.txt', 'w'))
# ---------------------------------------
sys.stdout.write('witaj świecie\n')
# ---------------------------------------
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print("log.txt")  # Pokazuje się w log.txt
sys.stdout.close()
sys.stdout = temp
print("jestem juz na konsoli ponownie")
# ---------------------------------------
print('%s %s %s' % ('mielonka', 'szynka', 'jajka'))
print('{0} {1} {2}'.format('mielonka', 'szynka', 'jajka'))




















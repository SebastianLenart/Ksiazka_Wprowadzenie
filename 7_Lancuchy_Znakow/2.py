"""
metody stringow:
S.capitalize()
S.center(width [, fill])
S.count(sub [, start [, end]])
S.encode([encoding [,errors]])
S.endswitch(suffix [, start [, end]])
S.expandtabs([tabsize])
S.find(sub[, start [, end]])
S.format(fmstr,*args,**kwargs)
S.index(sub[, start [, end]])
S.isalnum()
S.isalpha()
S.isdeciaml()
S.isdigit()
S.isidentifier()
S.islower()
S.isnumeric()
S.isprintable()
S.isspace()
S.istitle()
S.isupper()
S.join(iterable)
S.ljust(width [, fill])
S.lower()
S.lstrip([chars])
S.maketrans(x[, y[, z]])
S.partition(sep)
S.replace(old, new[, count])
S.rfind(sub [, start [, end]])
S.rindex(sub [, start [, end]])
S.rjust(width [, fill])
S.rpartition(sep)
S.rsplit([sep [, maxsplit]])
S.rstrip([chars])
S.split([sep [, maxsplit]])
S.splitlines([keepends])
S.startswitch(prefix [, start, [, end]])
S.strip([chars])
S.swapcase()
S.title()
S.translate(map)
S.upper()
S.zfill()

"""
a = "aa$bb$cc$dd"
print(a.replace("$", "OO"))
print(a.replace("$", "OO", 1))
where = a.find("c")
print(a[:where])
L = list(a)
print(list(L))
z = "".join(L)
print("z", z)
print(a.endswith("$dd"))
print(a.startswith("aa$"))

# print(sl)
template = "{a}, {b} oraz {c}"
print(template.format(a="hej", b = "Seba", c= "juhu"))

somelist = list("JAJKO")
ws = "pierwszy={0[0]}, trzeci={0[2]}".format(somelist)
print(ws)

wss = "1szy={0}, 2gi={1}".format(somelist[0], somelist[1])
print(wss)

parts = somelist[0], somelist[-1], somelist[1:3]
zz ="1szy={0}, 2gi={1}, 3ci={2}".format(*parts) # * rozdziela na oddzielne argumenty
print(zz)

import sys
q = "{0.platform:>10} = {1[item]:<10}".format(sys, dict(item="laptop"))
print(q)

ko = "{0:X}, {1:o}, {2:b}".format(255,255,255)
print(ko)







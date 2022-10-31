s = "mielonka"
print(s)
print(s.find("ie")) # 1
s = s.replace("ie", "YYYY")
print(s)
print("----------------------------------------------------")
line = "aaa,bbb,cccc,dd"
print(line.split(sep=",")) # ['aaa', 'bbb', 'cccc', 'dd']



print(dir(s))
print("----------------------------------------------------")
print(help(s.replace))

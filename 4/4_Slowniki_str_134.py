from pprint import pprint
# dict("wiek" : 40, "zawod" : "programista")
data = {
     "dane osobowe" : { "imie" : "robert", "nazwisko" : "Zielony"},
     "zawod" : ["programista", "inzynier"],
     "wiek" : 40.5
 }

print(data["zawod"][-1]) # inzynier
data["zawod"].append("serwisant")
pprint(data)
#-------------------------------------------------------------------------
print("----------")

# Ks = list(data.keys())
# Ks.sort()
# for key in Ks:
#     print(key, data[key])

# szybciej
for key in sorted(data):
    print(key, data[key])

# GET ??
value = data.get("wiek", 1) # ????
print(value)
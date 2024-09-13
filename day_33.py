# this program use directories method
dic={"mazhar":334,"amina":333}
print(dic["mazhar"])
print(dic["amina"])
print(dic)
print(dic.get("mazhar"))
print(dic.get("haseeb"))
print(dic.keys())

for info in dic.keys():
    print(dic[info])

print(dic.items())

for key,value in dic.items():
    print(f"the value corresponding to {key} is {value}")
    
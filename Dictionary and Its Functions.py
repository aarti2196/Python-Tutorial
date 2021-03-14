#Dictionary is collection of key and value pairs
d1 ={}
print(type(d1))

d2={
    "Name": "Arati","SurName":"Joshi",
    "Subject":{ "F":"Marathi", "B":"Hindi", "C":"English"}
}
print(d2["Subject"]["B"])
d2["Nivideta"]="Junk Food"
d2[100]="Police"
del d2 [100]
print(d2)
d3 = d2.copy()
del d3["Name"]
print(d2)
print(d2.get("Name"))
d2.update({"Leena":"IceCream"})
print(d2)
print(d2.keys())
print(d2.items())
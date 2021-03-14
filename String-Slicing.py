mystr = "arati is Rpa Developer"
print(mystr[0:5])
print(len(mystr))
print(mystr[0:22])
print (mystr[0:5:3])
name="Developer"
print(name[0:8:4])
print(name[0:])
print(name[0::])
print(name[::]) # Slice.. Skipping character according to condition if value is 2 then it will skip 1 after one
# character
#Negative slicing
print(name[-4:-1])
print(name[::2])
print(mystr.isalnum())
print(mystr.endswith("Developer"))
print(mystr.startswith("Arati"))
print(mystr.count("r"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.replace("is","Hello"))
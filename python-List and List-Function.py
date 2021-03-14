#python List and List Functions
grocery=["oil","powder","vimbar","ghee","bhindi","Lolipop",56]
print(grocery[6])
numbers=[1,2,3,4,5]
#print(numbers)
#print(numbers.sort())
#numbers.reverse()
#print(numbers[2])
print(numbers[1:5])
print(numbers[1:3])
mynumbers=[15,25,65,78,89]
print(mynumbers[1:4])
#it will take input numbers as 15,25,65,78 ()As index no
25,65,78
print(mynumbers[2:4])
#Extended Slice
print(numbers[::-1])# reverse of numbers
mynumbers.append(72)#Append Numbers
print(mynumbers)
num =[]
num.append(12)
num.append(56)
num.append(75)
print(num)
num.insert(1,62)
print(num)
num.remove(56)
print(num)
num.pop()
print(num)
new=[1,2,3,4,5]
new[1]=62
print(new)
tp =(1,2,3,4)
#tp [1] = 65 throw an error for tuple modification
print(tp) # throw an error for tuple.. tuple is an immutable object we cant modify tuple elements
# Tuple is immutable object
tp =('Rpa','sapui5','Angular','Javascript')
print(tp)
languages ="Angular","Angular","python" # Allow duplicate values 
print(languages)


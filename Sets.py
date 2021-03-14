s= set()
# print (type(s))
# s= set [1,2,3,4,5]
# s.add(65)
# s.add(6)
# print(s)
s.add(1)
s.add(2)
s.add(3)
#set take only unique Values
s1 = s.intersection({1,2})
print(s1,s)
s1 = s.isdisjoint(s)
s1 ={4,6}
print(s.isdisjoint(s1))
s.remove(2)
print(s)
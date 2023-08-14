doc =(1,2,[1,2])
doc[-1].append(4)
print(doc)

L =[1,2]
x = list(map(lambda x  : x** 2,L))
print(x)
for c in x:
    print(c)


print(enumerate([3]))
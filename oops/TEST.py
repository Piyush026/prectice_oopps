y  = {'a':5,'b':7}
x =  {'b':6,'d':10}

z = {**y, **x}
print(z)
j ="iodfnkkdzhu"
x ="gdjasd,gjdsgjj,djshuiw"
print(type(x))

print("split::", j.split(','))
print("ppp",[j[i:i+3] for i in range(0,len(j),3)])
ch = [i for i,d in enumerate(j) if d=='d']
print("ocurence:::::", ch)
len(x)
# isinstance()
x.lower()
x.isalnum()
x.isupper()
# x.replace()
print("index of j",j.index("k"))
# y.range()
# x.__reversed__()
b =x.capitalize()
b =x.casefold()


print(b)

myList = [3.5,7.8,8.9]
myList = [int(round(x)) for x in myList]
print(myList)
x = [1,2,3,4]
f = [1,11,22,33,44,3,4]

result = set(f) - set(x) # correct elements, but not yet in sorted order
print(sorted(result))
print(list(reversed(f)))
print(f[-1: :])




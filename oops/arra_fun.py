li = [1,2,3,4,5]
output = [3,4,5,1,2]
x =li[0:2]
li += x

print("lliii",li)
del li[0:2]
print(li)


l = [1, 2, 3, 4, 5, 6]
def rotate(lst, x):
    lst[:] = lst[-x:] + lst[:-x]

rotate(l, 2)
print( l)

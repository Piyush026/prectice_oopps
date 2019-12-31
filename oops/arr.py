import itertools

###########rotate list
li  =  [1,2,3,4,5]
lst = []
print(li[2:])
print(li[:2])

lst[:] = li[2:] + li[:2]

# lst[:] = li[-3:] + li[:-3]
print("rotate list",lst)

###########change !st element and last element in list

# li  = [4, 6, 88, 34, 7]
# a,*b,c = li
#
# li = c ,*b, a
# print(li)
#
#################### find the index of the element
from functools import reduce

li= [56,76,4,3,7,8,4,6,3]
print(len(li))
lst = ["geek","for","geek"]
lsst = ["geek for geek"]
print(lsst)
# for i in[i for i,x in enumerate(li) if x == 4]:
#     print(i)
for id, value in enumerate(lst):
    if value == "geek":
        print(id)
print(lst.index("geek"))
del lst[2]
print(lst)
########################## check element exist or not
li= [56,76,4,3,7,8,4,6,3]
for x in li:
    if x == 76:
        print(x)
    else:
        print("not exist")
print(li)

li *= 0
# li.clear()
print(li)

#################################3copy
li= [56,76,4,3,7,8,4,6,3]
l = li.copy()
# l =list(li)
print(l)


################################# occurence of en element
li= [56,76,4,3,7,8,4,6,3]
p = li.count(4)
print(p)
cnt = 0
for x in li:
    if (x==4):
        cnt += 1
print(cnt)


############### sum of list
li= [56,76,4,3,7,8,4,6,3]
print(sum(li))

som = 0
for x in li:

    som = som+x
print(som)
#####################################Find sum of frequency of given elements in the list

num =[1,2,4]
num2 = [2, 1, 2, 1, 3, 5, 2, 3]

print("sum of frequency",sum(num2.count(el) for el in num))

#################################zip function
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,3,4,5]

results = list(zip(my_strings, my_numbers))

print("zip",results)


#############################map function

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)




my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(map(lambda x, y: (x*y), my_strings, my_numbers))

print(results)

####################
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print("palindromes",palindromes)


############################
# Use map to print the square of each numbers rounded
# to two decimal places

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
mf_result = list(map(lambda x :round(x**3,2),my_floats))
print(mf_result)

################################
# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
mn_result = list(filter(lambda name :len(name)<=7,my_names))
print(mn_result)
########################
# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
reduce_result = reduce(lambda num1,num2: num1 if  num1 > num2 else num2, my_numbers)
print("reduce",reduce_result)

###########################accumulate
lis = [ 1, 3, 4, 10, 4 ]
z= list(itertools.accumulate(lis,lambda x,y:x+y))
print(z)
y = reduce(lambda x,y:x+y,lis)
print(y)
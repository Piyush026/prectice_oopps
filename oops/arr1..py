import itertools
from functools import reduce

list2 = [20, 10, 20, 1, 100]
print(min(list2))

#############################find N largest elements from a list

li = [81, 52, 45, 10, 3, 2, 96]
n=3
li.sort()
print(li[-3:])

###############################program to print even numbers in a list
li = [81, 52, 45, 10, 3, 2, 96]

l2 = list(filter(lambda x:x % 2 ==0,li ))
print("filter",l2)
###############################program to print odd numbers in a list


li = [81, 52, 45, 10, 3, 2, 96]

l2 = list(filter(lambda x:x % 2 !=0,li ))
print(l2)

#############################print all even numbers in a range start from 4 and end with 15
mp =[]
for x in range(4,15):
    mp.append(x)
# ch = list(filter(lambda y: y% 2==0,x))
print("mpp::::",mp)
ch = list(filter(lambda y: y% 2==0,mp))
print(ch)

############################### Python program to print positive Numbers in a List
list1 = [-10, 21, 4, -45, -66, 93, -11]
no  = list(filter(lambda x:(x>=0),list1))
print(no)

#################Python program to remove empty tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]

kkk = list(filter(None,tuples))
print(kkk)

#################################remove duplicate from list
l = [1,2,3,4,4,5,5,6,1]
print("duplicate",set(l))
z = set([x for x in l if l.count(x) > 1])
print("duplicate",z)
########################program to find Cumulative sum of a list
list5 = [10, 20, 30, 40, 50]
lt = []
s = 0
for x in list5:
    s +=x
    lt.append(s)
print("Cumulative",lt)
llll= list(itertools.accumulate(list5,lambda x,y:x+y))
print('Cumulative',llll)
tttt = reduce(lambda x,y:x+y,list5)
print("Cumulative",tttt)
########################## Break a list into chunks of size N in Python
my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
n = 5

x = list(divide_chunks(my_list, n))
print("divide_chunks",x)


def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]
yy =list(chunks(my_list,5))
print(yy)


#
# def better_grouper(inputs, n):
#     iters = [iter(inputs)] * n
#     return zip(*iters)
# re =list(better_grouper(my_list, 5))
# print(re)

#########################sum of two list
lt5 = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
print("map::::::::::::",lt5)



##############################Sort the values of first list using second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
newlt = list(zip(list2,list1))
z = [x for x, x in sorted(newlt)]
newlt.sort()
print(z)


########################palindrom

# x = ["piyush","madam"]
# y = "piyush"
# w = ""
# for i in y:
#     w = i + w
#     if (x == w):
#         print("YES")
# else:
#         print(w)
#
# z = list(filter(lambda word:word == word[::-1],x))
# print(z)

########################Reverse words in a given String in Python
# a = "I'm fall in love in jugnu"
#
# print(a[-1::-1])
#
# s =a.split()
# z= s[-1::-1]
# print(z)
# resullr =' '.join(s)
# print(resullr)
####################################remove i’th character from string in Python
# n = "jugnu and paglu"
# print(n[:2])
# print(n[3:])
# new_str = n[:2] + n[3:]
# print(new_str)
# k=n.replace('u', ' ',2)
# print(k)
# strA = "Game of Thrones"
# print(strA.replace('e', '', 2))
################################### check string in or not
# string = "geeks for geeks"
# sub_str = "kkk"
# z = sub_str in string
# print(z)
#################### print even word in given string
st = "This is a python language"
s = st.split(' ')
for x in s:
    if len(x)%2==0:
        print(x)
    else:
        print('no')


######################### check vovel in the string or not
vowels = "aeiouAEIOU"
s = "gksfrgk"
result = any(ch in vowels for ch in s)
print(result)

################################## Count from list
from collections import Counter
data = ['green','red','green','orange','green','red']
new = {x:data.count(x) for x in data}
print(new)
cc = Counter(new)
print(cc)

################################### same character in 2 string
str1 ='aabcddekll12@'
str2 ='bb2211@55k'
st1 = set(str1)
st2 = set(str2)
mat = st1&st2
print(str(len(mat)))

#################################  all duplicates from a given string in Python
from collections import OrderedDict

str1 = "geeksforgeeks"
ll = "".join(set(str1))

pp ="".join(OrderedDict.fromkeys(str1))
print("pp",pp)
print("ll",ll)


################################################# check if a string contains any special character
mystring ='Geeks2ForGeeks'
# x= any(not c.isalnum() for c in mystring)
# print(x)
print(mystring.isalnum())

#######################################3join and split

s1 = 'Geeks for Geeks'
re_s1 = s1.split(' ')
print(s1)
print(re_s1)
rr_s2 = '-'.join(re_s1)
print(rr_s2)

##############################merge three dict in one dict
import collections


test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
             {'it' : 5, 'is' : 7, 'best' : 8},
             {'CS' : 10}]
############
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, ... ]
x= [input[i:i+2] for i in range(0, len(input), 2)]
print(x)
########################sort dict

d = {'a': [1, 2, 3], 'c': ['one', 'two'], 'b': ['blah', 'bhasdf', 'asdf'], 'd': ['asdf', 'wer', 'asdf', 'zxcv']}
# print(sorted(d.values()))
for k in sorted(d):
    print(k, d[k])

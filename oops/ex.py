
x, y, z = 0, 0, 0

if x==1 or y == 1 or z == 1:
    print('passed')
else:
    print(x)

if 1 in (x, y,z ):
    print('passed')

if x or y or z:
    print('passed')

if any((x,y,z)):
    print('passed')

# def apply_discount(product, discount):
#     price = int(product['price'] * (1.0 - discount))
#     assert 0 <= price <= product['price']
#     return price
#
#
# shoes = {'name': 'Fancy Shoes', 'price': 14900}
# dis = apply_discount(shoes, 2.0)
# print(dis)


################
class MyClass:
    i = 123

    def __init__(self):
        self.i = 345


a = MyClass()
print(a.i)
print(MyClass.i)

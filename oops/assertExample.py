def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
dis = apply_discount(shoes, 2.0)
print(dis)
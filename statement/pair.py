#coding:utf-8

rows = [1, 2, 3, 17]

def cols():        # example of simple generator
    yield 56
    yield 2
    yield 1

x_product_pairs = ((i, j) for i in rows for j in cols())

for pair in x_product_pairs:
     print pair

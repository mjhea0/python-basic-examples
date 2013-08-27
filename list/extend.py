#coding:utf-8

a = [1, 2, 3]
b = [4, 5, 6]

#注意和append的区别
a.extend(b)

#[1, 2, 3, 4, 5, 6]
print a

#[4, 5, 6, [1, 2, 3, 4, 5, 6]]
b.append(a)
print b

list1 = ["One", "Two", "Three"]
list2 = ["Five", "Six"]

list1.extend(list2)
#['One', 'Two', 'Three', 'Five', 'Six']
print list1

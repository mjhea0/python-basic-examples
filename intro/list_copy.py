#coding:utf-8

def copy_list_with_none(a, my_list = None):
  if my_list is None:
    my_list = []
    my_list.append(a)
    return my_list

print copy_list_with_none('padding string', None)
print copy_list_with_none('padding string', [])

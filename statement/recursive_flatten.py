#coding:utf-8

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print list(flatten([[[1],2],3,4,[5,[6,7]],8]))

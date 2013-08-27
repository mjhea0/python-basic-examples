#coding:utf-8

def normal():
    def action():
        return spam        

    spam = 'ni'
    return action

act = normal()
print act()

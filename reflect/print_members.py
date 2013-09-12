import inspect

class User:
    name = "bob"
    
for x in inspect.getmembers(User):
    print x
    
print inspect.isclass(User)
print inspect.getmodule(User)
print inspect.getfile(User)
print inspect.getsourcefile(User)
print inspect.getsourcelines(User)
print inspect.getsource(User)
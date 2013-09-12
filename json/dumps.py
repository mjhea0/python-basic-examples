import json

str = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print str
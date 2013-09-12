import json
from StringIO import StringIO

io = StringIO()
json.dump(['streaming API'], io)
print io.getvalue()
import datetime

print(datetime.datetime.now())

import hashlib

mi_sha256 = hashlib.sha256()
mi_sha256.update("adfasdfasdfasdf".encode("utf8"))
print(mi_sha256.hexdigest())
import hmac
import hashlib
import base64
data = "Hello World!"
key = "abc"
print(hashlib.sha256(data.encode("utf8")).hexdigest())
print(hashlib.sha1(data.encode("utf8")).hexdigest())
sign = hmac.new(key.encode("utf8") , data.encode("utf8") , hashlib.sha1).digest() 
print(base64.b64encode(sign))
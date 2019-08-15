import time
import datetime
import json


def log(message, when=datetime.datetime.now()):
    print('%s: %s' % (when, message))


def log2(message, when=None):
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))


def decode(data, defult={}):
    try:
        return json.loads(data)
    except ValueError:
        return defult


def decode2(data, defult=None):
    if defult is None:
        defult = {}
    try:
        return json.loads(data)
    except ValueError:
        return defult


# log('Hi there!')
# time.sleep(0.1)
# log('Hi there!')


log2('Hi there!')
time.sleep(0.1)
log2('Hi there!')

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('bad data')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

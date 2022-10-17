import hashlib
#
# m = hashlib.md5()
# m.update(b"Hello")
# print(m.hexdigest())
# m.update(b"It's me")
# print(m.hexdigest())
# m.update(b"It's been a long time since last time we ...")
# print(m.hexdigest())
#
m2 = hashlib.md5()
m2.update("HelloIt's me".encode(encoding='utf-8'))
print(m2.hexdigest())
#
# s2 = hashlib.sha1()
# s2.update(b"HelloIt's me")
# print(s2.hexdigest())
#
# s224 = hashlib.sha224()
# s224.update(b"HelloIt's me")
# print(s224.hexdigest())
#
# s256 = hashlib.sha256()
# s256.update(b"HelloIt's me")
# print(s256.hexdigest())
#
# s384 = hashlib.sha384()
# s384.update(b"HelloIt's me")
# print(s384.hexdigest())
#
# s512 = hashlib.sha512()
# s512.update(b"HelloIt's me")
# print(s512.hexdigest())

import hmac

h = hmac.new(b'hello','abc天王盖地虎'.encode(encoding='utf-8'))
print(h.hexdigest())
print(h.digest())
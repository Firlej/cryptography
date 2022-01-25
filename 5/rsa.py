import sympy
from math import gcd


p = 31
q = 19

n = p*q

phi = (p-1)*(q-1)

e = sympy.randprime(100000, 1000000)
e = 7
while gcd(e,phi) != 1:
    e = sympy.randprime(100000, 1000000)

d = 463
while (e*d-1) % phi != 0:
    d+=1

public = (e, n)
private = (d, n)

print('p =', p)
print('q =', q)
print('n =', n)
print('phi =', phi)
print('public =', public)
print('private =', private)

# raw message
raw = 'message 123456789 message 123456789 message 123456789 message 123456789'
print(f"Raw message: {raw}")

# encoding
encoded = [pow(ord(c),e,n) for c in raw]
print(f"Encoded: {encoded}")

# decoding
decoded = "".join([chr(pow(i, d, n)) for i in encoded])
print(f"Decoded: {decoded}")

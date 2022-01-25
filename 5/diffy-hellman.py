import random
import sympy

n = 2 ** 127 - 1
g = 500008

x = random.randint(100000, 1000000)
X = pow(g, x, n)

y = random.randint(100000, 1000000)
Y = pow(g, y, n)

kA = pow(Y, x, n)
kB = pow(X, y, n)

print("A:",kA)
print("B:",kB)

def run():
	pass

if __name__ == '__main__':
	run()
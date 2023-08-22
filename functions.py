# Importing required modules
import math as Math
import cmath
import random as rand

# Version
version = 'MathBot | v 3.2'

# Constants
constants = ['pi', 'e', 'phi', 'ec', 'tau', 'π', 'φ', 'γ', 'τ']
constants2 = ['pi', 'e', 'phi', 'ec', 'tau', 'i', 'your mom']
pi = 3.1415926538979323846
e = 2.7182818284590452354
phi = 1.6180339887498948482
ec = 0.5772156649015328606
tau = 6.2831853077958647692
i = 0+1j
π = pi
φ = phi
γ = ec
τ = tau

# Functions
def joinArgs(arg, start):
	string = ""
	for idx in range(start, len(arg)):
		string = string + arg[i]
		if idx < len(arg) - 1:
			string = string + ' '
	return string

def calculate(expression: str):
	validSymbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
					'+', '-', '*', '/', '(', ')',
					'p', 'i', 'e', 'c', 'h', 't', 'a', 'u']
	for idx in range(len(expression)):
		if expression[idx] not in validSymbols:
			return ['Invalid input (expression) in command. Please try again.', 0xff0000]

	try:
		result = str(eval(expression))
		if result.endswith('j'):
			return [result[:-1]+'i', 0x66ffff]
		elif result.endswith('j)'):
			return [result[:-2]+'i)', 0x66ffff]
		else:
			return [result, 0x66ffff]
	except:
		return ['Invalid input (expression) in command. Please try again.', 0xff0000]

def pyTriangle(side1, side2):
	hypotenuse = (side1 * side1) + (side2 * side2)
	hypotenuse = Math.sqrt(hypotenuse)
	return str(hypotenuse)


def nthTermOfFib(n):
	# Formula: (φ^n - (1/φ)^n)/sqrt(5)
	val = Math.floor((Math.pow(phi, n) - Math.pow(1 - phi, n)) / Math.sqrt(5))
	return val


def nthRoot(A, N):
	# initially guessing a random number between 0 and 9
	xPre = rand.randint(0, 9)
	# smaller eps, denotes more accuracy
	eps = 0.00000000001
	# initializing difference between two roots by INT_MAX
	delX = 2147483647
	# xK denotes current value of x
	xK = 0.0
	# loop until we reach desired accuracy
	while (delX > eps):

		# calculating current value from previous value by newton's method
		xK = ((N - 1.0) * xPre + A / pow(xPre, N - 1)) / N
		delX = abs(xK - xPre)
		xPre = xK

	if Math.floor(xK) == xK:
		return int(xK)
	else:
		return xK

def convertVal(fromBase, toBase, value):
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
			   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
			   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
			   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
			   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			   '+', '/'
	]
	numbersToCheck = []
	for idx in range(fromBase):
		numbersToCheck.append(numbers[idx])
	val = 0
	for idx in range(len(value)):
		if value[len(value) - idx - 1] not in numbersToCheck:
			return ['Invalid number. Please try again.', 0xff0000]
		temp = numbers.index(value[len(value) - idx - 1])
		val += temp * int(Math.pow(fromBase, idx))
	temp = ''
	while val > 0:
		temp = temp + numbers[Math.floor(val % toBase)]
		val = Math.floor(val / toBase)
	result = ''
	for idx in range(len(temp)):
		result = result + temp[len(temp) - idx - 1]
	if result == '':
		result = '0'
	return [result, 0x66ffff]

def factor(value):
	n = value
	idx = 2
	factors = []
	while idx <= n // idx:
		while (n % idx == 0):
			factors.append(idx)
			n = n // idx
		idx += 1
	if n > 1:
		factors.append(int(n))
	return str(factors)

def nthTermOfSeq(n, seq):
	# Analyzes the seq string, and returns the first two terms of the sequence.
	t1 = None
	t2 = None
	cIdx = 0
	for idx in range(len(seq)):
		if seq[idx] == ',':
			if t1 == None:
				t1 = float(eval(seq[cIdx:idx]))
				cIdx=idx+1
			elif t2 == None:
				t2 = float(eval(seq[cIdx:idx]))
				cIdx=idx+1
	if t2 == None:
		t2 = float(eval(seq[cIdx:len(seq)]))
	# Actual term calculation
	d = t2 - t1
	d = t1 + (n - 1) * d
	if Math.floor(d) == d:
		return int(d)
	else:
		return d

def gSequence(n, r):
	result = 0
	for idx in range(n):
		p = Math.pow(r, idx)
		result += p
	if Math.floor(p) == p:
		return int(result)
	else:
		return result

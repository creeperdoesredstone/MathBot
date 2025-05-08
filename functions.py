# Importing required modules
import math as Math
import random as rand
from sympy import diff, symbols, solve, sympify



# Version
version = 'MathBot | v 3.8'

# Commands list
commands = ['help', 'ping', 'cmd_stats',
			'random', 'randint', 'roll', 'flip',
			'calc', 'root', 'factors', 'factorial', 'sum', 'solve', 'derive', 'properties', 'log', 'floor', 'ceil',
			'basecalc', 'convert',
			'permutations', 'combinations',
			'trig', 'radians', 'degrees', 'sidecalc', 'input', 'plot', 'logic',
			'pytriangle', 'fib', 'constant', 'term', 'g_series', 'g_sequence', 'prime']

# Constants
constants = ['pi', 'e', 'phi', 'ec', 'tau', 'π', 'φ', 'γ', 'τ']
constants2 = ['pi', 'e', 'phi', 'ec', 'tau', 'i', 'your mom']
pi = 3.1415926538979323846264338327950288419716939937510582097494459230781640628620899
e = 2.71828182845904523536028747135266249775724709369995957496696762772407663035354759
phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189
ec = 0.5772156649015328606065120900824024310421593359399235

tau = 6.2831853077958647692337839024855821615565655464351730825
i = 0 + 1j
π = pi
φ = phi
γ = ec
τ = tau
yourmom = "Your mom."
# Functions
# Utilities
primes = []

def joinList(arg, start, delimiter=""):
	string = ""
	for idx in range(start, len(arg)):
		if idx < len(arg) - 1:
			string = string + str(arg[idx]) + delimiter
		else:
			string = string + str(arg[idx])
	return string

def splitString(string):
	list = []
	for idx in string:
		list.append(idx)
	return list

def isSquare(value):
	s = int(Math.sqrt(value))
	return s*s == value

def isFib(n):
	return isSquare(5*n*n+4) or isSquare(5*n*n-4)

def isBell(n):
	return 

def cosine(value):
	return Math.cos(value*pi/180)

def isPrime(k):
	# Corner cases
	if (k <= 1):
		return False
	if (k == 2 or k == 3):
		return True
	# Below 5 there is only two prime numbers 2 and 3
	if (k % 2 == 0 or k % 3 == 0):
		return False
	# Using concept of prime number can be represented in form of (6*k + 1) or(6*k - 1)
	for i in range(5, 1 + int(k ** 0.5), 6):
		if (k % i == 0 or k % (i + 2) == 0):
			return False
	return True
 
# Function which gives prime at position n
def nthPrime(n):
    i = 2
    while(n > 0):
 
        # Each time if a prime number found decrease n
        if(isPrime(i)):
            n -= 1
 
        i += 1  # Increases i to go ahead
 
    i -= 1  # Since decrement of k is being done before increment of i, so i should be decreased by 1
    return i

# Functions
def calculate(expression: str, isEquation=False):
	validSymbols = [
	 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '^', '%',
	 '(', ')', '.', ' ', 'p', 'i', 'e', 'c', 'h', 't', 'a', 'u'
	]
	if isEquation:
		validSymbols.append('x')
	if "**" in expression:
		return [
			 'You still remember when ** was supported?', 0xfcba03
			]
	e = splitString(expression)
	for idx in range(len(e)):
		if e[idx] not in validSymbols:
			return [
			 'Invalid input (expression) in command. Please try again. Error number 1', 0xff0000
			]
		if e[idx] == '^':
			e[idx] = '**'

	ex = joinList(e, 0)
	try:
		result = str(eval(ex))
		if result.endswith('j'):
			return [result[:-1] + 'i', 0x66ffff]
		elif result.endswith('j)'):
			return [result[:-2] + 'i)', 0x66ffff]
		else:
			return [result, 0x66ffff]
	except OverflowError:
		return ['Calculation too large to handle!', 0xff0000]
	except:
		return ['Invalid input (expression) in command. Please try again. Error number 2', 0xff0000]

def pyTriangle(side1, side2):
	hypotenuse = (side1 * side1) + (side2 * side2)
	hypotenuse = Math.sqrt(hypotenuse)
	return str(hypotenuse)

def nthTermOfFib(n):
	# Formula: (φ^n - (1/φ)^n)/√(5)
	val = Math.floor((Math.pow(phi, n) - Math.pow(1 - phi, n)) / Math.sqrt(5))
	return val

def nthRoot(A, N):
	# initially guessing a random number between 1 and 9
	xPre = rand.randint(1, 9)
	# smaller eps, denotes more accuracy
	eps = 0.00000000001
	# initializing difference between two roots by INT_MAX
	delX = 2147483647
	# xK denotes current value of x
	xK = 0.0
	# loop until we reach desired accuracy
	while (delX > eps):

		# calculating current value from previous value by newton's method
		xK = ((N - 1.0) * xPre + A / Math.pow(xPre, N - 1)) / N
		delX = abs(xK - xPre)
		xPre = xK

	if Math.floor(xK) == xK:
		return int(xK)
	else:
		return xK

def convertVal(fromBase, toBase, value):
	numbers = [
	 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
	 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
	 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
	 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
	 'y', 'z', '+', '/', ' '
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
	if n > 1 or len(factors) == 0:
		factors.append(int(n))
	return factors

def nthTermOfSeq(n, seq):
	# Analyzes the seq string, and returns the first two terms of the sequence.
	t1 = None
	t2 = None
	cIdx = 0
	for idx in range(len(seq)):
		if seq[idx] == ',':
			if t1 == None:
				t1 = float(eval(seq[cIdx:idx]))
				cIdx = idx + 1
			elif t2 == None:
				t2 = float(eval(seq[cIdx:idx]))
				cIdx = idx + 1
	if t2 == None:
		t2 = float(eval(seq[cIdx:len(seq)]))
	# Actual term calculation
	d = t2 - t1
	d = t1 + (n - 1) * d
	if Math.floor(d) == d:
		return int(d)
	else:
		return d

def gSequence(n, start, r):
	n = int(n)
	start = float(start)
	r = float(r)
	result = start
	for idx in range(n - 1):
		result *= r
	if Math.floor(result) == result:
		return int(result)
	else:
		return result

def generateSeq(n, s, d):
	sequence = []
	for idx in range(n):
		t = s + (d * idx)
		if Math.floor(t) == t:
			sequence.append(int(t))
		else:
			sequence.append(t)
	return sequence

def solveEquation(e):  # Solves the equation given
	acceptedSymbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
					   '+', '-', '*', '/', '^', '=', ' ', '.', '(', ')', 'x']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	if "=" not in e:
		return ['Invalid input (equation) in command. Please try again.', 0xff0000]
	e = e.replace(' ', '')
	e = e.replace('=', '-(')
	e = splitString(e)
	for i in range(len(e)):
		if e[i] not in acceptedSymbols:
			print(i)
			return ['Invalid input (equation) in command. Please try again.', 0xff0000]
		if e[i] == '^':
			e[i] = '**'
		if e[i] in numbers and len(e) > i+1:
			if e[i + 1] == 'x':
				e.insert(i+1, '*')
				i += 1
	e.append(')')
	x = symbols('x')
	exp = joinList(e, 0)
	if x == x:
		e = sympify(exp)
	result = solve(e)
	result = joinList(result, 0, " or ")
	result = splitString(result.lower())
	for i in range(len(result)):
		if i <= len(result) - 4:
			if result[i] + result[i+1] + result[i+2] + result[i+3] == 'sqrt':
				result[i] = '√'
				result[i+1] = ''; result[i+2] = ''; result[i+3] = ''
	result = joinList(result, 0)
	return [result, 0x66ffff]

def derive(e):
	e = splitString(e)
	acceptedSymbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
					   '+', '-', '*', '/', '^', '=', ' ', '.', '(', ')', 'x']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for i in range(len(e)):
		if e[i] not in acceptedSymbols:
			print(i)
			return ['Invalid input (equation) in command. Please try again.', 0xff0000]
		if e[i] == '^':
			e[i] == '**'
		if e[i] in numbers and len(e) > i+1:
			if e[i + 1] == 'x':
				e.insert(i+1, '*')
				i += 1
	e = joinList(e, 0)
	x = symbols('x')
	if x == x:
		e = sympify(e)
	result = str(diff(e))
	result = splitString(result)
	for i in range(len(result)):
		if result[i] == '*':
			if result[i-1] in numbers and result[i+1] == 'x':
				result[i] = ''
			if result[i+1] == '*':
				result[i] = '^'
				result[i+1] = ''
	result = joinList(result, 0)
	return [result, 0x66ffff]

def logicOp(op, val1, val2):
	operations = ['and', 'or', 'nor', 'xor', 'nand', 'xnor']
	binary = ['0', '1']
	if op.lower() not in operations:
		return ['Invalid command!', 'Invalid input (operation) in command. Please try again.', 0xff0000]
	for i in val1:
		if i not in binary:
			return ['Invalid command!', 'Invalid input (val1) in command. Please try again.', 0xff0000]
	for i in val2:
		if i not in binary:
			return ['Invalid command!', 'Invalid input (val2) in command. Please try again.', 0xff0000]
	length = len(val1)
	if len(val2) > length:
		length = len(val2)
	val1 = eval(convertVal(2, 10, val1)[0])
	val2 = eval(convertVal(2, 10, val2)[0])
	invert = False
	if op.lower() == 'and':
		result = val1 & val2
	if op.lower() == 'or':
		result = val1 | val2
	if op.lower() == 'nor':
		result = (val1 | val2)
		invert = True
	if op.lower() == 'xor':
		result = val1 ^ val2
	if op.lower() == 'nand':
		invert = True
		result = (val1 & val2)
	if op.lower() == 'xnor':
		result = (val1 ^ val2)
		invert = True
	temp = splitString(str(result))
	if result < 0:
		temp.pop(0)
	print(temp)
	result = joinList(temp, 0)
	result = convertVal(10, 2, str(result))[0]
	temp = splitString(result)
	while len(temp) < length:
		temp.insert(0, '0')
	while len(temp) > length:
		temp.pop(0)
	if invert:
		for i in range(len(temp)):
			if temp[i] == '1':
				temp[i] = '0'
			else:
				temp[i] = '1'
	result = joinList(temp, 0)
	
	return ['Output', result, 0x66ffff]

def permutations(n, r):
	# Returns the result of nPr, where
	# n = total number of objects
	# r is number of objects to select
	result = Math.factorial(n) // Math.factorial(n - r)
	return int(result)

def combinations(n, r):
	# Returns the result of nCr, where
	# n = total number of objects
	# r is number of objects to select
	result = Math.factorial(n) // (Math.factorial(r) * Math.factorial(n - r))
	return int(result)

def findSideLength(inputs, mode, places):
	i1 = inputs[0]; i2 = inputs[1]; i3 = inputs[2]
	if mode == "rhs":
    	# Hypoteneuse, side, 90
    	# Pythagorean theorem
		sideLength = Math.sqrt((i1*i1)-(i2*i2))
	if mode == "rss":
		sideLength = Math.sqrt((i1*i1)+(i2*i2))
	if mode == "rha":
		# Hypoteneuse, angle, opp/adj
		if i3 == 1:
			sideLength = i1*Math.sin(Math.radians(i2))
		if i3 == 2:
			sideLength = i1*Math.cos(Math.radians(i2))
	if mode == "rsa":
		# Opposite side, angle, opp/adj
		if i3 == 1:
			sideLength = i1/Math.tan(Math.radians(i2))
		if i3 == 2:
			sideLength = i1*Math.tan(Math.radians(i2))
	if mode == "asa":
		# Angle, side, angle
		# Uses the law of sines: sin(A)/a = sin(B)/b = sin(C)/c
		print("First given angle:", i1)
		print("Second given angle:", i3)
		print("Given side:", i2)
		sinA = Math.sin(Math.radians(i1))
		sinB = Math.sin(Math.radians(i3))
		sideLength = sinA/(sinB/i2)
	if mode == "sas":
		# Side, angle, side
    	# Uses the law of cosines: c^2 = a^2 = b^2 - 2ab(cos(theta))
		sideLength = Math.sqrt((i1*i1) + (i3*i3) - (2*i1*i3*Math.cos(Math.radians(i2))))
	sideLength = round(sideLength, places)
	if Math.floor(sideLength) == sideLength:
		return int(sideLength)
	else:
		return sideLength

def findArea(sideLength, shape):
	if shape == 'square':
		result = sideLength * sideLength
	if shape == 'triangle':
		result = Math.sqrt(3)/4 * sideLength * sideLength
	if shape == 'pentagon':
		result = 0.25 * Math.sqrt(5*(5+2*Math.sqrt(5))) * sideLength * sideLength
	if shape == 'hexagon':
		result = 3/2 * Math.sqrt(3) * sideLength * sideLength
	if shape == 'heptagon':
		result = 7/4 * Math.sqrt(5*(5+2*Math.sqrt(5))) * sideLength * sideLength
	if Math.floor(result) == result:
		result = int(result)
	return result

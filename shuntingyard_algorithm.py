def numberIndex(mystring):
	myindex = []
	length = len(mystring)
	for i in range(0, length):
		if isNumber(mystring[i]) and (i == 0 or mystring[i - 1] == '(' or isOperator(mystring[i - 1])):
			myindex.append(i)
		if isNumber(mystring[i]) and (i == length - 1 or mystring[i + 1] == ')' or isOperator(mystring[i + 1])):
			myindex.append(i)
	return myindex

def pullNumbers(mystring):
	'+'.split(mystring)

# Check if the list is empty or not
def isEmpty(mylist):
	return (len(mylist) == 0)

# Removes the last item in the list
def popLast(mylist):
	last = mylist[-1]
	del mylist[-1]
	return last

# Returns the value of the last item
def lastValue(mylist):
	return mylist[-1]

# Checks whether the input is a number or not
def isNumber(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

# Checks whether the input is an operator or not
def isOperator(i):
	operator = ['+', '-', '*', '/']
	if i in operator:
		return True
	return False

def opPriority(operator):
	if operator == '*' or operator == '/':
		return 2
	elif operator == '+' or operator == '-':
		return 1
	else:
		return 0

# Converts from infix to postfix notation (Reverse polish)
def inTOpost(mystring, array_postfix):
	# An array used to store operators. It acts like a stack
	mystack = []

	# Index for the numbers
	myindex = numberIndex(mystring)
	i = 0
	while i < len(mystring):
		# If the character is a number, push it to the postfix string
		if i in myindex:
			array_postfix.append(mystring[myindex[0] : myindex[1] + 1])
			i = myindex[1] + 1
			if i == len(mystring):
				i -= 1
			del myindex[0 : 2]

		# If the character is '(', push it to the stack
		if mystring[i] == '(': 
			mystack.append('(')

		# If the character is an operator:
		# 1) If the priority value of the incoming operator is:
		# 		* less than (or equal to) the last item in the stack,
		# 		=> Push all items in the stack to the postfix string until the last item in the stack
		# 		has lower priority than the incoming operator
		# 2) Or if the stack is empty, put the operator into it anyway

		# The break command quits the loop when the stack is empty, which helps prevent the opPriority()
		# from being initialized (opPriority() returns the priority of the last value of the stack,
		# but since the stack has already been empty; we will receive a 'list index out of range')
		
		elif isOperator(mystring[i]): 
			if (not isEmpty(mystack)):
				while (opPriority(mystring[i]) <= opPriority(lastValue(mystack))):
					array_postfix.append(popLast(mystack))
					if len(mystack) == 0:
						break
			mystack.append(mystring[i])

		# If the character is ')', we will push all the items in the stack to the postfix until we see a '('
		elif mystring[i] == ')':
			while lastValue(mystack) != '(':
				array_postfix.append(popLast(mystack))
			popLast(mystack)

		i += 1

	# Put the remaining items to the postfix
	while (not isEmpty(mystack)):
		array_postfix.append(popLast(mystack))

def calcPostfix(mystring):
	mystack = []
	for item in mystring:
		if isNumber(item):
			mystack.append(float(item))
		elif isOperator(item):
			a = (popLast(mystack))
			b = (popLast(mystack))
			if item == '+':
				c = b + a
			elif item == '-':
				c = b - a
			elif item == '*':
				c = b  * a
			elif item == '/':
				c = b / a
			mystack.append(c)
		else:
			print 'Syntax error'
			return -1

	return popLast(mystack)

if __name__ == '__main__':

	# [2 1]
	# [* +]
	#print isNumber('n')
	#a = raw_input('Hello: ')
	b = []
	c = []
	d = []
	inTOpost('1+2', b)

	print b

	print calcPostfix(b)
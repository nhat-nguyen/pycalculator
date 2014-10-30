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


def removeSign(number):
	if '/' in number or '*' in number:
		return "syntax error"
	countNegative = 0
	number = number.replace('+', '')
	for i in number:
		if i == '-':
			countNegative += 1
	number = number.replace('-', '')
	if countNegative % 2 == 0:
		return float(number)
	else:
		return -float(number)

# Returns a list containing the index of each number in the string
def numberIndex(mystring, myindex):
	length = len(mystring)
	for j in range(0, length):
		if isNumber(mystring[j]) or mystring[j] == '-':
			myindex.append(j)
			break			
	if j == length - 1:
		myindex.append(j)
	else:
		for i in range(j, length - 1):
			if isNumber(mystring[i]) and (isOperator(mystring[i + 1]) or mystring[i + 1] == ')'):
				myindex.append(i)
				break
		i += 1
		while i < length:
			if isOperator(mystring[i]):
				if isNumber(mystring[i - 1]) or mystring[i - 1] == ')':
					for j in range(i + 1, length):
						if isNumber(mystring[j]) or isOperator(mystring[j]):
							myindex.append(j)
							break
					for k in range(j, length - 1):
						if isNumber(mystring[k]) and (isOperator(mystring[k + 1]) or mystring[k + 1] == ')'):
							myindex.append(k)
							break
				i += 2
			else:
				i += 1

		i = length - 1
		
		while i >= 0:
			if isNumber(mystring[i]):
				myindex.append(i)
				break
			i -= 1
			

def opPriority(operator):
	if operator == '*' or operator == '/':
		return 2
	elif operator == '+' or operator == '-':
		return 1
	else:
		return 0

# Converts from infix to postfix notation (Reverse polish)
def inTOpost(mystring, arrayPostFix):
	# An array used to store operators. It acts like a stack
	mystack = []
	myindex = []
	# Index for the numbers
	numberIndex(mystring, myindex)
	i = 0
	while i < len(mystring):
		# If the character is a number, push it to the postfix string
		if i in myindex:
			number = mystring[myindex[0] : myindex[1] + 1]
			number = removeSign(number)

			if not isNumber(number):
				return 0

			arrayPostFix.append(number)
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
					arrayPostFix.append(popLast(mystack))
					if len(mystack) == 0:
						break
			mystack.append(mystring[i])

		# If the character is ')', we will push all the items in the stack to the postfix until we see a '('
		elif mystring[i] == ')':
			while lastValue(mystack) != '(':
				arrayPostFix.append(popLast(mystack))
			popLast(mystack)

		i += 1

	# Put the remaining items to the postfix
	while (not isEmpty(mystack)):
		arrayPostFix.append(popLast(mystack))

	return 1

def calcPostfix(mystring):
	mystack = []
	for item in mystring:
		if isNumber(item):
			mystack.append(float(item))
		elif isOperator(item):
			if len(mystack) == 0:
				return "syntax error"
			a = popLast(mystack)
			if len(mystack) == 0:
				return "syntax error"
			b = popLast(mystack)
			if item == '+':
				c = b + a
			elif item == '-':
				c = b - a
			elif item == '*':
				c = b  * a
			elif item == '/':
				c = b / a
			mystack.append(c)
	results = popLast(mystack)
	if int(results) == results:
		return int(results)
	return results
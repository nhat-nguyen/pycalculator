from shuntingyard import *
from Tkinter import *

class calcWindow:

	def add(self, number):
		if ((not isOperator(number)) and len(self.v.get()) == 0) or (len(self.v.get()) > 0) or number == '-':
			self.textbox.insert(END, number)
	
	def clearTextbox(self):
		self.textbox.delete(0, END)
		del self.postfix[:]

	def printResults(self):
		# remove all the spaces in the input
		infix = self.v.get()
		infix = infix.replace(' ', '')
		noError = inTOpost(infix, self.postfix)
		self.textbox.delete(0, END)
		if (noError):
			result = calcPostfix(self.postfix)
		else:
			result = u"\u2612"+" Error. " + u"\u2639"
		self.textbox.insert(0, result)

		del self.postfix [1:]

	def __init__(self, master):
		self.clearme = False
		self.postfix = []
		window = Frame(master)		
		window.pack()

		self.v = StringVar()

		self.textbox = Entry(window, textvariable = self.v)

		self.textbox.grid(row = 0, columnspan = 6)

		self.nine = Button(window, text = '9', command = lambda: self.add(9)).grid(row = 1, column = 1)
		
		self.eight = Button(window, text = '8', command = lambda: self.add(8)).grid(row = 1, column = 2)

		self.seven = Button(window, text = '7', command = lambda: self.add(7)).grid(row = 1, column = 3)

		self.six = Button(window, text = '6', command = lambda: self.add(6)).grid(row = 2, column = 1)

		self.five = Button(window, text = '5', command = lambda: self.add(5)).grid(row = 2, column = 2)

		self.four = Button(window, text = '4', command = lambda: self.add(4)).grid(row = 2, column = 3)

		self.three = Button(window, text = '3', command = lambda: self.add(3)).grid(row = 3, column = 1)

		self.two = Button(window, text = '2', command = lambda: self.add(2)).grid(row = 3, column = 2)

		self.one = Button(window, text = '1', command = lambda: self.add(1)).grid(row = 3, column = 3)

		self.zero = Button(window, text = '0          ', command = lambda: self.add(0)).grid(row = 4, column = 1, columnspan = 2)

		self.dot = Button(window, text = '.', command = lambda: self.add('.')).grid(row = 4, column = 3)

		self.plus = Button(window, text = '+', command = lambda: self.add('+')).grid(row = 4, column = 4)

		self.minus = Button(window, text = '-', command = lambda: self.add('-')).grid(row = 3, column = 4)

		self.multiply = Button(window, text = unichr(215), command = lambda: self.add('*')).grid(row = 2, column = 4)

		self.divide = Button(window, text = unichr(247), command = lambda: self.add('/')).grid(row = 1, column = 4)

		self.openBrackets = Button(window, text = '(', command = lambda: self.add('(')).grid(row = 2, column = 5)

		self.closeBrackets = Button(window, text = ')', command = lambda: self.add(')')).grid(row = 3, column = 5)

		self.equal = Button(window, text = '=', command = lambda: self.printResults()).grid(row = 4, column = 5)

		self.clear = Button(window, text = 'C', command = lambda: self.clearTextbox()).grid(row = 1, column = 5)

root = Tk()

root.minsize(width = 200, height = 150)
root.maxsize(width = 200, height = 150)
root.wm_title(unichr(961) + unichr(611) + " calculator")

Nhat = calcWindow(root)
root.mainloop()
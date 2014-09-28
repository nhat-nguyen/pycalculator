""""""""""""""""""""
import os

import sys

from shuntingyard_algorithm import *

from Tkinter import *

class calcWindow:
	def change(self):
		self.clearme = not self.clearme

	def add(self, number):
		if self.clearme:
			self.textbox.delete(0, END)
			self.clearme = False
		self.textbox.insert(END, number)
	
	def clearTextbox(self):
		self.textbox.delete(0, END)

	def printResults(self):
		self.clearme = True
		infix = self.v.get()
		postfix = []
		inTOpost(infix, postfix)
		self.textbox.delete(0, END)
		self.textbox.insert(0, calcPostfix(postfix))

	def __init__(self, master):

		self.clearme = False

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

		self.zero = Button(window, text = '0', command = lambda: self.add(0)).grid(row = 4, column = 1)

		self.dot = Button(window, text = '.', command = lambda: self.add('.')).grid(row = 4, column = 2)

		self.one = Button(window, text = '+', command = lambda: self.add('+')).grid(row = 1, column = 4)

		self.one = Button(window, text = '-', command = lambda: self.add('-')).grid(row = 2, column = 4)

		self.one = Button(window, text = '*', command = lambda: self.add('*')).grid(row = 1, column = 5)

		self.one = Button(window, text = '/', command = lambda: self.add('/')).grid(row = 2, column = 5)

		self.lbrackets = Button(window, text = '(', command = lambda: self.add('(')).grid(row = 3, column = 4)

		self.rbrackets = Button(window, text = ')', command = lambda: self.add(')')).grid(row = 3, column = 5)

		self.equal = Button(window, text = '=', command = lambda: self.printResults()).grid(row = 4, column = 3, columnspan = 3)

root = Tk()

Nhat = calcWindow(root)

root.mainloop()
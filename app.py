from zury import Framework
from Tkinter import *
import sys
import os

class MainApplication():
	def __init__(self):
		self.framework = Framework()
		self.app = self.framework.BrowserApplication()
		self.width = 800
		self.height = 600
	def __menu__(self):
		self.menu = Menu(self.app.window)
		filemenu = Menu(self.menu)
		filemenu.add_command(label="Exit", command=sys.exit)
		self.menu.add_cascade(label="File", menu=filemenu)
		self.app.window.config(menu=self.menu)
	def run(self, title):
		self.app.window.title = title
		self.app.window.show(self.width, self.height, True, False)
	def size(self, width, height):
		self.width = width
		self.height = height

root = MainApplication()
root.size(800, 600)
root.app.window.setDefaultURL("https://iplo.tk/apps/aad/game.php")
root.run("Angels & Demons")
from sys import *
import os
from Tkinter import *
from tkFileDialog import *

class AppWindow():
	def __init__(self):
		self.root = Tk()
		self.menu = Menu(self.root)
		self.title = "app"
	def minSize(self, width, height):
		self.root.minsize(width=width, height=height)
	def maxSize(self, width, height):
		self.root.maxsize(width=width, height=height)
	def fixedSize(self, width, height):
		self.root.minsize(width=width, height=height)
		self.root.maxsize(width=width, height=height)
	def launch(self):
		self.root.config(menu=self.menu)
		self.root.title(self.title)
		self.root.mainloop()

class Framework():
	def __init__(self):
		if __name__ == 'main':
			print("Loading Frameworks")
	class BrowserApplication():
		def __init__(self):
			import webkitui
			self.window = webkitui.Window()
	class TextApplication():
		def __init__(self):
			if self.defaults == True:
				self.window = AppWindow()
				self.window.fixedSize(400,400)
				self.txt = self.makeBase(self.window, 400, 400)
				self.txt.pack(self.window.root)
		def makeBase(self, window, width, height):
			root = window.root
			txt = Text(root, width=400, height=400)
			txt.delete(0.0, END)
			return txt
		def makeMenu(self, window, new, openf, save, saveas):
			filemenu = Menu(window.menu)
			filemenu.add_command(label="New", command=new)
			filemenu.add_command(label="Open", command=openf)
			filemenu.add_command(label="Save", command=save)
			filemenu.add_command(label="Save As", command=saveas)
			window.menu.add_cascade(label="File", menu=filemenu)
			return window

def Compiler(name,version,directory,appfile, iconfile, keepassets, extrafiles):
	print("Writing Files...")
	f = open(directory+"/build.py", "w")
	f.write("'''\nUsage IN TERMINAL .. :\n\tpython build.py py2app\n'''\n\nfrom setuptools import setup\n\nAPP = [\"zuryapp.py\"]\nDATA_FILES = [('', ['images']), ('', ['Audio'])]\nOPTIONS = {\n\t'iconfile': \""+iconfile+"\"\n}\n\nsetup(\n\tname = \""+name+"\",\n\tversion = \""+version+"\",\n\tapp = APP,\n\tdata_files = DATA_FILES,\n\toptions = {'py2app': OPTIONS},\n\t  setup_requires = ['py2app']\n)")
	f.close()

	import os
	print("Making Nessecary Files...")
	os.system("touch zuryapp.py")
	print("Files Created!")
	print("Changing Permissions of Created Files...")
	os.system("chmod 755 zuryapp.py")
	print("Copying Your App File...")
	os.system("cp "+appfile+" zuryapp.py")
	print("Copied!")
	print("")
	print("Making Directory(s)...")
	os.system("mkdir images")
	os.system("mkdir Audio")
	print("")
	print("Using Py2App...")
	os.system("python build.py py2app")
	print("Moving Zury Over...")
	os.system("cp zury.py dist/"+name+".app/Contents/Resources")
	os.system("cp webkitui.py dist/"+name+".app/Contents/Resources")
	os.system("cp qt.py dist/"+name+".app/Contents/Resources")
	os.system("cp cocoa.py dist/"+name+".app/Contents/Resources")
	os.system("cp gtk.py dist/"+name+".app/Contents/Resources")
	os.system("cp win32.py dist/"+name+".app/Contents/Resources")
	os.system("cp __init__.py dist/"+name+".app/Contents/Resources")
	os.system("cp main.py dist/"+name+".app/Contents/Resources")
	for f in extrafiles:
		os.system("cp "+f+" dist/"+name+".app/Contents/Resources")
	print("Moving App Back Directory...")
	os.system("mv dist/"+name+".app ./")
	print("Deleting Unneccesary Folders...")
	os.system("rm -rd dist")
	os.system("rm -rd build")
	os.system("rm -rf zuryapp.py")
	os.system("rm -rf build.py")
	if keepassets:
		os.system("rm -rf zury.pyc")
		print("Done!")
	else:
		os.system("rm -rd Audio")
		os.system("rm -rd images")
		os.system("rm -rf zury.pyc")
		print("Done!")

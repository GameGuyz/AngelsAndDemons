import Tkinter
import os
import webbrowser
import sys
import main

argv = sys.argv

if __name__ == 'main':
	print("Error: [Erno 1] This is a module!")
else:
	class Window():
		def __init__(self):
			self.title = "Zury"
			self.defaulturl = "https://google.com"
		def show(self, width, height, r, f):
			main.create_window(self.title, self.defaulturl, width, height, r, f)
		def change_url(self,url_token):
			main.load_url(url_token)
		def setDefaultURL(self,url_token):
			self.defaulturl = url_token
import pygame
pygame.init()

from code.View import View
from code.Label import Label
from code.Button import Button


class TitleView(View):
	def __init__(
		self,
		_base_view):
		
		super(
			TitleView,
			self).__init__(
				_base_view.image,
				_base_view.clock)
				
	
	def create_objects(self):
	
		# Title of the game.
		config = dict()
		config["text"] = "KoolSzavak"
		config["font_size"] = 100
		config["bg_colour"] = (200, 200, 200)		
		self.title = Label(
			config)
		self.title.align_top(
			self.rect)
		self.title.align_centerw(
			self.rect)
			
		# Subtitle of the game.
		config = dict()
		config["text"] = "Tanulj magyar szavakat!"
		config["font_size"] = 50
		config["fg_colour"] = (100, 100, 100)
		config["bg_colour"] = (200, 200, 200)
		config["top"] = 100
		self.subtitle = Label(
			config)
		self.subtitle.align_centerw(
			self.rect)
			
		# Start the game.
		config = dict()
		config["text"] = "Start"
		config["font_size"] = 40		
		config["top"] = 200
		self.start = Button(
			config)
		self.start.align_centerw(
			self.rect)
			
		# Options.
		config = dict()
		config["text"] = "Options"
		config["font_size"] = 40			
		config["top"] = 250
		self.options = Button(
			config)
		self.options.align_centerw(
			self.rect)
			
		# End the game.
		config = dict()
		config["text"] = "Exit"
		config["font_size"] = 40			
		config["top"] = 300
		self.exit = Button(
			config)
		self.exit.align_centerw(
			self.rect)		
		
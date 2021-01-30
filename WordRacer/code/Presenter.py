import pygame
pygame.init()

import random

from code.View import View
from code.WordDictionary import WordDictionary


class Presenter(object):
	def __init__(self):
		
		config = dict()
		config["filepath"] = "woeijfoiwjfo.wef"
		self.word_dictionary = WordDictionary(
			config)
			
		self.window = pygame.display.set_mode(
			(640, 480))		
		self.clock = pygame.time.Clock()
			
		self.view = View(
			self.window,
			self.clock)
		
		self.view.attach_quit(
			self.on_quit)
			
		self.view.word.attach_activeevent(
			self.hello)
		self.view.word.attach_clicked(
			self.clicked)
		self.view.word2.attach_clicked(
			self.clicked)
		
			
	
	def run(self):
	
		self.view.run()				
		pygame.display.quit()	
			
	
	def on_quit(self,
		_sender,
		_eventargs):
		
		self.view.running = False
	
	
	def hello(self,
		_sender,
		_eventargs):
		
		print("Hello")
	
	
	def clicked(
		self,
		_sender,
		_eventargs):
		_sender.set_background((
			random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)))
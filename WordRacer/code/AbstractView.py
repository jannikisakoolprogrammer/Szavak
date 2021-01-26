import pygame
pygame.init()

from code.IView import IView
import abc
from code.Observable import Observable


class AbstractView(Observable, IView):

	actors = [] # List that contains actor instances.
	user_input = []

	def play(self):
		# Do pygame stuff.
		print("test123")
		
		self.read()
		self.inform()
		self.update()
		self.draw()
		
		# pygame.display.update()
		# pygame.display.draw()
	
	
	def stop(self):
		return
	
	
	@abc.abstractmethod
	def read(self):
		# User input etc.
		user_input = []
		# Read here.
	
	@abc.abstractmethod
	def update(self):
		pass
	
	@abc.abstractmethod
	def draw(self):
		pass
	
	
	@abc.abstractmethod
	def test123(self):
		pass
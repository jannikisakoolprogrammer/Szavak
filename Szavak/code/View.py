import pygame
pygame.init()

from code.EventSprite import EventSprite
from code.Word import Word

config = dict()
config["font_name"] = ""
config["font_size"] = 20
config["anti_aliasing"] = True
config["fg_colour"] = (0, 0, 0)
config["bg_colour"] = (255, 0, 0)
config["top"] = 400
config["left"] = 200	


class View(EventSprite):

	def __init__(self,
		_window,
		_clock):
	
		super(View, self).__init__()
		
		self.image = _window
		self.rect = self.image.get_rect()
		self.clock = _clock
		
		self.create_objects();
		
		self.sprites = pygame.sprite.Group()
			
		self.running = True		
		
		for attr, value in self.__dict__.items():
			if isinstance(
				value,
				EventSprite):
				self.sprites.add(
					value)
		
		
	def run(self):

		while self.running:
			events = pygame.event.get()
			self.update(events) # Global window events.
			self.sprites.update(events)
						
			self.image.fill((255, 255, 255))
			
			self.sprites.draw(
				self.image)

			pygame.display.update()
			self.clock.tick(30)	
	
	
	def create_objects(self):
		
		self.word = Word(
			config)
			
		config["top"] = 300
		config["left"] = 500
		self.word2 = Word(
			config)
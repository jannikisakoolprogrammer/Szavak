import pygame
pygame.init()

from code.Observable import Observable


class EventSprite(pygame.sprite.Sprite):
	def __init__(
		self):
		
		super(EventSprite, self).__init__()
		
		self.quit = Observable()
		self.activeevent = Observable()
		self.clicked = Observable()
		
	
	def attach_quit(self,
		_callback):
		
		self.quit.attach(
			_callback)
	
	
	def attach_activeevent(self,
		_callback):
		
		self.activeevent.attach(
			_callback)
	
	
	def attach_clicked(
		self,
		_callback):
		
		self.clicked.attach(
			_callback)
				
	
	def update(
		self,
		_events = []):
		
		for e in _events:
			self.handle_events(
				e)

	
	
	def handle_events(
		self,
		_e):

		if _e.type == pygame.KEYDOWN:
			if _e.key == pygame.K_ESCAPE:
				self.quit.inform(
					self,
					_e)
		
		elif _e.type == pygame.MOUSEBUTTONDOWN:
			points = pygame.mouse.get_pos()
			if self.rect.collidepoint(
				points) == True:
				self.clicked.inform(
					self,
					_e)
		
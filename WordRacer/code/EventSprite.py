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
		self.hover = Observable()
		self.blur = Observable()
		
		
		self.hover_active = False		
		
	
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
		
		elif _e.type == pygame.MOUSEMOTION:
			if self.rect.collidepoint(
				_e.pos) == True:
				self.hover_active = True
				self.hover.inform(
					self,
					_e)
			
			elif not self.rect.collidepoint(
				_e.pos) == True and self.hover_active == True:
				self.hover_active = False
				self.blur.inform(
					self,
					_e)
	
	
	def align_left(
		self,
		_parent_rect):
		
		self.rect.left = 0
	
	
	def align_right(
		self,
		_parent_rect):
		
		self.rect.right = _parent_rect.width
	
	
	def align_top(
		self,
		_parent_rect):
		
		self.rect.top = 0
	
	
	def align_bottom(
		self,
		_parent_rect):
		
		self.rect.bottom = _parent_rect.height
		
	
	def align_centerw(
		self,
		_parent_rect):
		
		self.rect.centerx = _parent_rect.width / 2
	
	
	def align_centerh(
		self,
		_parent_rect):
		
		self.rect.centery = _parent_rect.height / 2
		
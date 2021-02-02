import pygame
pygame.init()

from code.EventSprite import EventSprite


class Label(EventSprite):
	def __init__(
		self,
		_config = dict()):
		
		super(Label, self).__init__()
		
		self.config = _config
		
		self.text = self.config["text"] if "text" in self.config else "<example-text>"
		self.font_name = self.config["font_name"] if "font_name" in self.config else "Lucida Console"
		self.font_size = self.config["font_size"] if "font_size" in self.config else 30
		self.anti_aliasing = self.config["anti_aliasing"] if "anti_aliasing" in self.config else True
		self.fg_colour = self.config["fg_colour"] if "fg_colour" in self.config else (0, 0, 0)
		self.bg_colour = self.config["bg_colour"] if "bg_colour" in self.config else (255, 0, 0)
		self.top = self.config["top"] if "top" in self.config else 100
		self.left = self.config["left"] if "left" in self.config else 200

		self.font = pygame.font.SysFont(
			self.font_name,
			self.font_size)
		
		self.image = self.font.render(
			self.text,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)
			
		self.rect = self.image.get_rect()
		
		self.rect.top = self.top
		self.rect.left = self.left
	
	
	def set_text(
		self,
		_text):
		
		self.text = _text	
	
	
	def render(
		self):

		self.image = self.font.render(
			self.text,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)
			
		old_top = self.rect.top
		old_left = self.rect.left
		self.rect = self.image.get_rect()
		
		self.rect.top = old_top
		self.rect.left = old_left

		
	def set_background(self, _colour):
		self.image = self.font.render(
			self.text,
			self.anti_aliasing,
			self.fg_colour,
			_colour)
		
		
	def handle_events(
		self,
		_e):

		super(Label, self).handle_events(_e)			
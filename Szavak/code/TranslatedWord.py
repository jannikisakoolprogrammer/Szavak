import pygame
pygame.init()

from code.EventSprite import EventSprite


class TranslatedWord(EventSprite):
	def __init__(
		self,
		_config = dict(),
		_word = "egy",
		_translation = "eins"):
		
		super(TranslatedWord, self).__init__()
		
		self.config = _config
		
		self.word = self.config["word"] if "word" in self.config else "egy"
		self.translation = self.config["translation"] if "translation" in self.config else "eins"		
		self.font_name = self.config["font_name"] if "font_name" in self.config else "Lucida Console"
		self.font_size = self.config["font_size"] if "font_size" in self.config else 20
		self.anti_aliasing = self.config["anti_aliasing"] if "anti_aliasing" in self.config else True
		self.fg_colour = self.config["fg_colour"] if "fg_colour" in self.config else (0, 0, 0)
		self.bg_colour = self.config["bg_colour"] if "bg_colour" in self.config else (255, 0, 0)
		self.top = self.config["top"] if "top" in self.config else 100
		self.left = self.config["left"] if "left" in self.config else 200

		self.font = pygame.font.SysFont(
			self.font_name,
			self.font_size)
		
		self.image = self.font.render(
			self.word,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)
			
		self.rect = self.image.get_rect()
		
		self.rect.top = self.top
		self.rect.left = self.left
	
	
	def set_background(self, _colour):
		self.image = self.font.render(
			self.word,
			self.anti_aliasing,
			self.fg_colour,
			_colour)
	
	
	def render(
		self):
		self.image = self.font.render(
			self.word,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)	
		self.height = self.rect.centery
		self.rect = self.image.get_rect()
		self.rect.centery = self.height
		
	def handle_events(
		self,
		_e):

		super(TranslatedWord, self).handle_events(_e)

		if _e.type == pygame.KEYDOWN:
			if _e.key == pygame.K_RETURN:
				self.activeevent.inform(
					self,
					_e)		
	
	
	def set_word_info(
		self,
		_native,
		_translated,
		_correct_word_idx):
		
		self.native = _native
		self.translated = _translated
		self.correct_word_idx = _correct_word_idx
		
		self.word = self.translated
		
		self.render()
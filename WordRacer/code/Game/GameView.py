import pygame
pygame.init()

from code.View import View
from code.Word import Word
from code.TranslatedWord import TranslatedWord


class GameView(View):
	
	def __init__(
		self,
		_base_view):
		
		super(
			GameView,
			self).__init__(
				_base_view.image,
				_base_view.clock)
	
	
	def create_objects(
		self):
		
		config = dict()
		config["bg_colour"] = (230, 230, 230)
		config["fg_colour"] = (0, 0, 0)
		config["font_size"] = 25
		
		# Word 1
		config["top"] = 0
		self.word1 = Word(
			config)
		self.word1.align_centerw(
			self.rect)			
		
		# Word 2
		config["top"] = 50
		self.word2 = Word(
			config)
		self.word2.align_centerw(
			self.rect)	
			
		# Word 3
		config["top"] = 100
		self.word3 = Word(
			config)
		self.word3.align_centerw(
			self.rect)			
			
		# Word 4
		config["top"] = 150
		self.word4 = Word(
			config)
		self.word4.align_centerw(
			self.rect)				
			
		# Word 5
		config["top"] = 200
		self.word5 = Word(
			config)
		self.word5.align_centerw(
			self.rect)				
			
		# Translated word
		config["top"] = 400
		config["font_size"] = 25
		self.translated_word = TranslatedWord(
			config)
		self.translated_word.align_centerw(
			self.rect)
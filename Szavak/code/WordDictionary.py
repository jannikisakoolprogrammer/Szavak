import pygame
pygame.init()

import sys


class WordDictionary(object):
	
	def __init__(
		self,
		_config = dict()):
		
		self.config = _config
		
		self.filepath = self.config["filepath"] if "filepath" in self.config else sys.exit("Filename not given")
		


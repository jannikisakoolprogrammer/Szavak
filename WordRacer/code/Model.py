import sys
import random

class Model(object):
	
	def __init__(
		self,
		_config = dict()):
		
		self.config = _config
		
		self.filepath = self.config["filepath"] if "filepath" in self.config else sys.exit("Filename not given")
		
		self.load_words()
		self.fetch_words()
	
	def load_words(
		self):
		
		self.lines = dict()
		
		with open(
			self.filepath) as file_handle:			
			self.lines = file_handle.readlines()
	
	
	def fetch_words(
		self):
		
		# Randomly fetch N words		
		self.selected_word_pairs = dict()
		
		random.shuffle(self.lines)
		
		n_words = 5
		
		self.chosen_word_idx = random.randint(
			0,
			n_words)
		
		for x in range(n_words):
			l = self.lines[x]
			split_l = l.split("-")
			self.selected_word_pairs[split_l[0].strip()] = split_l[1].strip()
		
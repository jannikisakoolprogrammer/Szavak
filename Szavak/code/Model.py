import sys
import random

class Model(object):
	
	def __init__(
		self,
		_config = dict()):
		
		self.config = _config
		
		self.filepath = self.config["filepath"] if "filepath" in self.config else sys.exit("Filename not given")
		
		self.load_words()
		#self.fetch_words()
	
	def load_words(
		self):
		
		self.lines = dict()
		
		with open(
			self.filepath,
			"r",
			-1,
			"utf-8") as file_handle:			
			self.lines = file_handle.readlines()
		
		self.total_words = len(self.lines)
		random.shuffle(self.lines)
		self.lines_tuple = tuple(self.lines)
		self.counter = -1
	
	
	def fetch_words(
		self):

		if self.counter + 1 == self.total_words:
			return True
			
		self.counter += 1			
			
		word_indexes = []
		word_indexes.append(
			self.counter)
			
		# Now fetch four other indexes, but don't fetch the current one..
		indexes = list()
		for x in range(0, self.total_words):
			indexes.append(x)
		indexes.remove(self.counter)
		
		for x in range(4):
			idx = random.choice(indexes)
			word_indexes.append(
				idx)
			indexes.remove(idx)
		
		# Now we have five indexes.
		# The self.counter == indexes one is the correct one.
		
		# Now shuffle this list
		random.shuffle(word_indexes)
		
		# Now load the lines/words.
		
		# Randomly fetch N words		
		self.selected_word_pairs = dict()
		#
		#random.shuffle(self.lines)
		
		n_words = 5
		
		self.chosen_word_idx = self.counter
		
		for x in word_indexes:
			l = self.lines_tuple[x]
			split_l = l.split("-")
			self.selected_word_pairs[x] = (split_l[0].strip(), split_l[1].strip())
			
		
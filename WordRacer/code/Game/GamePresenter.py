import time
import pygame
pygame.init()

from code.Presenter import Presenter


class GamePresenter(Presenter):
	def __init__(
		self,
		_model,
		_view,
		_parent_presenter):
		
		super(
			GamePresenter,
			self).__init__(
				_model,
				_view,
				_parent_presenter)
		
		self.load_next_words()
		
		# Connect event handlers to words.
		words = (
			self.view.word1,
			self.view.word2,
			self.view.word3,
			self.view.word4,
			self.view.word5)
		for w in words:
			w.hover.attach(
				self.button_on_hover)
			w.blur.attach(
				self.button_on_blur)
			w.clicked.attach(
				self.word_clicked)

		
		self.run()
		
		
	def button_on_hover(
		self,
		_sender,
		_eventargs):
		
		_sender.on_hover()
	
	
	def button_on_blur(
		self,
		_sender,
		_eventargs):
		
		_sender.on_blur()	

	
	def word_clicked(
		self,
		_sender,
		_eventargs):

		if _sender.native == self.view.translated_word.native:
			# Correct - Mark clicked word green.
			_sender.mark_green()
		else:
			# Incorrect - Mark clicked word red.
			_sender.mark_red()			
			
		# Update view and pause for 2 seconds.
		self.view.sprites.draw(
			self.view.image)
		pygame.display.update()		
		time.sleep(1)
		# Load next word.
		self.load_next_words()
	
	
	def load_next_words(
		self):
		
		self.model.load_words()
		self.model.fetch_words()
		
		words = (
			self.view.word1,
			self.view.word2,
			self.view.word3,
			self.view.word4,
			self.view.word5)
			
		for x in range(len(words)):
			words[x].set_word_info(
				self.model.selected_word_pairs[x][0],
				self.model.selected_word_pairs[x][1],
				self.model.chosen_word_idx)
			words[x].align_centerw(
				self.view.rect)
		
		self.view.translated_word.set_word_info(
			self.model.selected_word_pairs[self.model.chosen_word_idx][0],
			self.model.selected_word_pairs[self.model.chosen_word_idx][1],
			self.model.chosen_word_idx)
		self.view.translated_word.align_centerw(
			self.view.rect)
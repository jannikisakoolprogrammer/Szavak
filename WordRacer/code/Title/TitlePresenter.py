import pygame
pygame.init()

from code.Presenter import Presenter
from code.Game.GameView import GameView
from code.Game.GameModel import GameModel
from code.Game.GamePresenter import GamePresenter


class TitlePresenter(Presenter):
	def __init__(
		self,
		_model,
		_view,
		_parent_presenter):
		
		super(
			TitlePresenter,
			self).__init__(
				_model,
				_view,
				_parent_presenter)
		
		# Connect event handlers to start button.
		self.view.start.hover.attach(
			self.button_on_hover)
		self.view.start.blur.attach(
			self.button_on_blur)
			
		# Connect event handlers to options button.
		self.view.options.hover.attach(
			self.button_on_hover)
		self.view.options.blur.attach(
			self.button_on_blur)
		
		# Connect event handlers to exit button.
		self.view.exit.hover.attach(
			self.button_on_hover)
		self.view.exit.blur.attach(
			self.button_on_blur)
		self.view.exit.clicked.attach(
			self.button_quit_clicked)			
	
	
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
		
	
	def button_quit_clicked(
		self,
		_sender,
		_eventargs):
		self.view.running = False
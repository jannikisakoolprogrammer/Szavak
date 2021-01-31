import pygame
pygame.init()

import random




class Presenter(object):
	def __init__(self,
		_model,
		_view,
		_parent_presenter = None):
		
		self.model = _model
		self.view = _view
		
		self.view.attach_quit(
			self.on_quit)

		self.parent_presenter = _parent_presenter
			
	
	def run(self):
	
		self.view.run()				
		pygame.display.quit()	
			
	
	def on_quit(self,
		_sender,
		_eventargs):
		
		self.view.running = False
	
	
	def hello(self,
		_sender,
		_eventargs):
		
		view = GameView(
			self.view.image,
			self.view.clock)
		model = GameModel(
			self.model)		
		presenter = GamePresenter(
			model,
			view,
			self)
		presenter.run()
	
	
	def clicked(
		self,
		_sender,
		_eventargs):
		_sender.set_background((
			random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)))
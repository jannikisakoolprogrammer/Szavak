import pygame
pygame.init()

from code.Presenter import Presenter


class GamePresenter(Presenter):
	def __init__(
		self,
		_model,
		_view,
		_base_presenter):
		
		super(
			GamePresenter,
			self).__init__(
				_model,
				_view)
		
		config = dict()
		config["filepath"] = "data"
		self.model = _model
		self.view = _view
		self.parent_presenter = _base_presenter
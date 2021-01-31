import sys
import random

from code.Model import Model

class TitleModel(Model):
	
	def __init__(
		self,
		_base_model,
		_config = dict()):
		
		super(
			TitleModel,
			self).__init__(
				_base_model.config)
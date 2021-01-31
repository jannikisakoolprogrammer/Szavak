from code.Model import Model


class GameModel(object):
	
	def __init__(
		self,
		_base_model,
		_config = dict()):
		
		self.base_model = _base_model
		self.config = _config
		
		
		
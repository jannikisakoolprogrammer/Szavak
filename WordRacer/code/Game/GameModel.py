from code.Model import Model


class GameModel(Model):
	
	def __init__(
		self,
		_base_model,
		_config = dict()):
		
		super(
			GameModel,
			self).__init__(
				_base_model.config)
import abc


class IView(abc.ABC):
	
	@abc.abstractmethod
	def play(self):
		pass
	
	
	@abc.abstractmethod
	def stop(self):
		pass
	
	
	@abc.abstractmethod
	def inform(self):
		pass
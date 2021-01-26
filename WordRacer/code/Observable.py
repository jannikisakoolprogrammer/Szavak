class Observable(object):

	observers = []
	
	
	def __init__(self):
		pass
	
	
	def attach(self,
		_observer):
		
		self.observers.Append(
			_observer)
	
	
	def inform(self):
		
		for observer in self.observers:
			observer.act()
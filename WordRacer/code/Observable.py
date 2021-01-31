class Observable(object):
	
	def __init__(self):
		
		self.observers = list()
	
	
	def attach(self,
		_callback):
		
		if not _callback in self.observers:
			self.observers.append(_callback)
		
	
	def remove(self,
		_callback):
		
		if _callback in self.observers:
			self.observers.remove(_callback)
	
	
	def inform(self,
		_sender,
		_event):
	
		for callback in self.observers:
			callback(
				_sender,
				_event)
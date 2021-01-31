from code.Label import Label


class Button(Label):

	def __init__(
		self,
		_config = dict()):
		
		super(
			Button,
			self).__init__(_config)
		
		self.fg_colour_hover = self.config["fg_colour_hover"] if "fg_colour_hover" in self.config else (200, 150, 100)
		self.bg_colour_hover = self.config["bg_colour_hover"] if "bg_colour_hover" in self.config else (100, 50, 20)
		

	def on_hover(
		self):
		
		self.image = self.font.render(
			self.text,
			self.anti_aliasing,
			self.fg_colour_hover,
			self.bg_colour_hover)
	
	
	def on_blur(
		self):
		
		self.image = self.font.render(
			self.text,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)
import pygame
pygame.init()

config = dict()
config["font_name"] = ""
config["font_size"] = 20
config["anti_aliasing"] = True
config["fg_colour"] = (0, 0, 0)
config["bg_colour"] = (255, 0, 0)
config["top"] = 400
config["left"] = 200


class Observable(object):
	
	def __init__(self):
		
		self.observers = dict()
	
	
	def attach(self,
		_observer,
		_callback):
	
		self.observers[_observer] = _callback
		
	
	def remove(self,
		_observer):
		
		if _observer in self.observers:
			del self.observers[_observer]
	
	
	def inform(self,
		_sender,
		_event):
	
		for observer, callback in self.observers.items():
			callback(
				_sender,
				_event)


class EventSprite(pygame.sprite.Sprite):
	def __init__(
		self):
		
		super(EventSprite, self).__init__()
		
		self.quit = Observable()
		self.activeevent = Observable()
		
	
	def attach_quit(self,
		_observer,
		_callback):
		
		self.quit.attach(
			_observer,
			_callback)
		
		
	
	def update(
		self,
		_events = []):
		
		for e in _events:
			print(e)
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					self.quit.inform(
						self,
						e)
		
		
		


class Word(EventSprite):
	def __init__(
		self,
		_config = dict(),
		_word = "egy",
		_translation = "eins"):
		
		super(Word, self).__init__()
		
		self.config = _config
		
		self.word = self.config["word"] if "word" in self.config else "egy"
		self.translation = self.config["translation"] if "translation" in self.config else "eins"		
		self.font_name = self.config["font_name"] if "font_name" in self.config else ""
		self.font_size = self.config["font_size"] if "font_size" in self.config else 20
		self.anti_aliasing = self.config["anti_aliasing"] if "anti_aliasing" in self.config else True
		self.fg_colour = self.config["fg_colour"] if "fg_colour" in self.config else (0, 0, 0)
		self.bg_colour = self.config["bg_colour"] if "bg_colour" in self.config else (255, 0, 0)
		self.top = self.config["top"] if "top" in self.config else 100
		self.left = self.config["left"] if "left" in self.config else 200

		self.font = pygame.font.SysFont(
			self.font_name,
			self.font_size)
		
		self.image = self.font.render(
			self.word,
			self.anti_aliasing,
			self.fg_colour,
			self.bg_colour)
			
		self.rect = self.image.get_rect()
		
		self.rect.top = self.top
		self.rect.left = self.left


class Presenter(object):
	def __init__(self,
		_word):
		self.word = _word
		self.word.attach_quit(
			self,
			self.on_quit)
		
		self.running = True
			
	
	def run(self):
		clock = pygame.time.Clock()

		window = pygame.display.set_mode(
			(640, 480))

		while self.running:
			events = pygame.event.get()
			self.word.update(events)
						
			window.fill((255, 255, 255))
			
			window.blit(
				self.word.image,
				self.word.rect)
			pygame.display.update()
			clock.tick(30)		
			
		pygame.display.quit()
	
			
	
	def on_quit(self,
		_sender,
		_eventargs):
		self.running = False
		

word = Word(
	config)
	
presenter = Presenter(word)
presenter.run()



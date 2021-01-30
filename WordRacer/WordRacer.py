import pygame
pygame.init()

import random
import sys

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


class EventSprite(pygame.sprite.Sprite):
	def __init__(
		self):
		
		super(EventSprite, self).__init__()
		
		self.quit = Observable()
		self.activeevent = Observable()
		self.clicked = Observable()
		
	
	def attach_quit(self,
		_callback):
		
		self.quit.attach(
			_callback)
	
	
	def attach_activeevent(self,
		_callback):
		
		self.activeevent.attach(
			_callback)
	
	
	def attach_clicked(
		self,
		_callback):
		
		self.clicked.attach(
			_callback)
				
	
	def update(
		self,
		_events = []):
		
		for e in _events:
			self.handle_events(
				e)

	
	
	def handle_events(
		self,
		_e):

		if _e.type == pygame.KEYDOWN:
			if _e.key == pygame.K_ESCAPE:
				self.quit.inform(
					self,
					_e)
		
		elif _e.type == pygame.MOUSEBUTTONDOWN:
			points = pygame.mouse.get_pos()
			if self.rect.collidepoint(
				points) == True:
				self.clicked.inform(
					self,
					_e)
		
		
		


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
	
	
	def set_background(self, _colour):
		self.image = self.font.render(
			self.word,
			self.anti_aliasing,
			self.fg_colour,
			_colour)
		
		
	def handle_events(
		self,
		_e):

		super(Word, self).handle_events(_e)

		if _e.type == pygame.KEYDOWN:
			if _e.key == pygame.K_RETURN:
				self.activeevent.inform(
					self,
					_e)		


class WordDictionary(object):
	
	def __init__(
		self,
		_config = dict()):
		
		self.config = _config
		
		self.filepath = self.config["filepath"] if "filepath" in self.config else sys.exit("Filename not given")


class View(EventSprite):

	def __init__(self,
		_window,
		_clock):
	
		super(View, self).__init__()
		
		self.image = _window
		self.rect = self.image.get_rect()
		self.clock = _clock
		
		self.running = True	
		self.create_objects();
		
		self.sprites = pygame.sprite.Group()
		self.sprites.add(
			self)
		self.sprites.add(
			self.word)
		self.sprites.add(
			self.word2)
		
	def run(self):

		while self.running:
			events = pygame.event.get()
			self.update(events) # Global window events.
			self.sprites.update(events)
						
			self.image.fill((255, 255, 255))
			
			self.sprites.draw(
				self.image)

			pygame.display.update()
			self.clock.tick(30)	
	
	
	def create_objects(self):
		
		self.word = Word(
			config)
			
		config["top"] = 300
		config["left"] = 500
		self.word2 = Word(
			config)
		


class Presenter(object):
	def __init__(self):
		
		config = dict()
		config["filepath"] = "woeijfoiwjfo.wef"
		self.word_dictionary = WordDictionary(
			config)
			
		self.window = pygame.display.set_mode(
			(640, 480))		
		self.clock = pygame.time.Clock()
			
		self.view = View(
			self.window,
			self.clock)
		
		self.view.attach_quit(
			self.on_quit)
			
		self.view.word.attach_activeevent(
			self.hello)
		self.view.word.attach_clicked(
			self.clicked)
		self.view.word2.attach_clicked(
			self.clicked)
		
			
	
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
		
		print("Hello")
	
	
	def clicked(
		self,
		_sender,
		_eventargs):
		_sender.set_background((
			random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)))
		
	
presenter = Presenter()
presenter.run()
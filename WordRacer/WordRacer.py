import pygame
pygame.init()


class Word(pygame.sprite.Sprite):
	def __init__(
		self,
		_word,
		_translation):
		
		super(Word, self).__init__()
		
		self.word = _word
		self.translation = _translation
	
		self.font = pygame.font.SysFont(
			"",
			20)
		
		self.image = self.font.render(
			self.word,
			True,
			(0, 0, 0),
			(255, 0, 0))
		self.rect = self.image.get_rect()
		

word = Word("egy", "eins")

clock = pygame.time.Clock()
running = True

window = pygame.display.set_mode(
	(640, 480))

while running:
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_ESCAPE:
				running = False
				
	window.fill((255, 255, 255))
	
	window.blit(
		word.image,
		word.rect)
	pygame.display.update()
	clock.tick(30)
	
	
pygame.display.quit()
	

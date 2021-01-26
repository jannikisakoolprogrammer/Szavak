import abc

import pygame
pygame.init()


class IViewTitle(abc.ABC):
	
	@abc.abstractmethod
	def getBox(self):
		pass
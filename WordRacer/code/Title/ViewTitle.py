from code.Title.IViewTitle import IViewTitle
from code.AbstractView import AbstractView

import pygame
pygame.init()


class ViewTitle(IViewTitle,AbstractView):
	
	def test123(self):
		print("eiojoiwejf")
	
	
	def getBox(self):
		print("oink")
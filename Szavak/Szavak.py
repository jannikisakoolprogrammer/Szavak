import pygame
pygame.init()

import random
import sys

from code.View import View
from code.Presenter import Presenter
from code.Model import Model

from code.Title.TitlePresenter import TitlePresenter
from code.Title.TitleView import TitleView
from code.Title.TitleModel import TitleModel

config = dict()
config["filepath"] = "data"
model = Model(
	config)
	
window = pygame.display.set_mode(
	(640, 480))		
clock = pygame.time.Clock()
	
view = View(
	window,
	clock)
			
presenter = Presenter(
	model,
	view)

# Title
title_model = TitleModel(
	model)

title_view = TitleView(
	view)

title_presenter = TitlePresenter(
	title_model,
	title_view,
	presenter)
	
title_presenter.run()
pygame.display.quit()	
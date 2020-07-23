import random
import pygame

class Coin:
  def __init__(self):
    x = random.randint(0,780)
    y = random.randint(100,584)
    self.rect = pygame.Rect(x,y,7,7)
    self.isHidden = False
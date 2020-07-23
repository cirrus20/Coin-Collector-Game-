#Import stuff
import pygame

from pygame.locals import *

from coin import Coin

#Setting up
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.init()

BLUE = pygame.Color(0,170,255)
BLACK = pygame.Color(8,13,13)
GREEN = pygame.Color(8,100,60)
speed_x = 0
speed_y = 0

player = pygame.Rect(390,290,14,14)

#Defining Movements
def move_left():
  global speed_x
  speed_x = -8
def move_right():
  global speed_x
  speed_x = 8
def move_up():
  global speed_y
  speed_y = 8
def move_down():
  global speed_y
  speed_y = -8

def movement_loop():
  global speed_x,speed_y,player
  player.centerx += speed_x
  player.centery -= speed_y
  speed_x = 0
  speed_y = 0

#Make 100 coins
list_of_coins = []

for x in range(100):
  list_of_coins.append(Coin())

  def render_coin_loop(screen):
    global list_of_coins
    global GREEN

    for coin in list_of_coins:
      if coin.isHidden == False:
        screen.fill(GREEN, coin.rect)

score = 0

#collision
def collision_loop():
  global list_of_coins
  global player
  global score

  for coin in list_of_coins:
    if player.colliderect(coin.rect) and coin.isHidden == False:
      coin.isHidden = True
      score += 1

#Main
def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit(0)
      pygame.event.pump()
      key = pygame.key.get_pressed()

      if key[K_UP]:
        move_up()
      if key[K_RIGHT]:
        move_right()
      if key[K_DOWN]:
        move_down()
      if key[K_LEFT]:
        move_left()

      movement_loop()
      collision_loop()
      clock.tick(60)
      screen.fill(BLACK)
      screen.fill(BLUE,player)
      render_coin_loop(screen)
      pygame.display.flip()

main()
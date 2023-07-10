#Setup
import pygame, sys
from pygame.locals import QUIT
pygame.init()
screen_info = pygame.display.Info()
#Display setup
size = (width, height) = (screen_info.current_w,screen_info.current_h)
screen = pygame.display.set_mode(size)
#Clock variable
clock = pygame.time.Clock()
#Screen color
color = (3,86,252)

def main():
  while True:
    #This is the game loop
    #Frame rate and visual filling
    clock.tick(65)
    screen.fill(color)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    #Screen rendering
    pygame.display.flip()
if __name__ == '__main__':
  main()
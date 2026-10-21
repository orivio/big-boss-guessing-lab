import pygame
import random

pygame.init()

clock = pygame.time.Clock()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

states = ["Graveyard", "House", "Forest", "Pumpkin"]

gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (128, 128, 128), (0, 0, WIDTH/2, HEIGHT/2)) #grave
    pygame.draw.rect(screen, (105, 42, 42), (WIDTH/2, 0, WIDTH, HEIGHT/2))#house
    pygame.draw.rect(screen, (25, 124, 50), (0, HEIGHT/2, WIDTH/2, HEIGHT)) #forestr
    pygame.draw.rect(screen, (125, 80, 10), (WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)) #pumpijn

    pygame.display.flip()

pygame.quit()

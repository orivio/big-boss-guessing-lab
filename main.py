import pygame
import random

pygame.init()

clock = pygame.time.Clock()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

states = ["Graveyard", "House", "Forest", "Pumpkin"]
transition_matrix = [
    [0.10, 0.45, 0.30, 0.15],
    [0.35, 0.10, 0.40, 0.15],
    [0.25, 0.35, 0.15, 0.25],
    [0.40, 0.20, 0.20, 0.20]
]

current_state = 1
next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
ambush_decision = 0
score = 0
rounds = 0


gameloop = True #TODO ADD SCORE N STUFF
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        ambush_decision = 0
        rounds += 1
        if(current_state == ambush_decision):
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"The monster escaped! Score: {score}")
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
    elif keys[pygame.K_2]:
        ambush_decision = 1
        rounds += 1
        if(current_state == ambush_decision):
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"The monster escaped! Score: {score}")
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
    elif keys[pygame.K_3]:
        ambush_decision = 2
        rounds += 1
        if(current_state == ambush_decision):
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"The monster escaped! Score: {score}")
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
    elif keys[pygame.K_4]:
        ambush_decision = 3
        rounds += 1
        if(current_state == ambush_decision):
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"The monster escaped! Score: {score}")
            current_state = next_state
            next_state = random.choices(range(4), weights = transition_matrix[current_state], k = 1)[0]
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (128, 128, 128), (0, 0, WIDTH/2, HEIGHT/2)) #grave
    pygame.draw.rect(screen, (105, 42, 42), (WIDTH/2, 0, WIDTH, HEIGHT/2))#house
    pygame.draw.rect(screen, (25, 124, 50), (0, HEIGHT/2, WIDTH/2, HEIGHT)) #forestr
    pygame.draw.rect(screen, (125, 80, 10), (WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)) #pumpijn

    font = pygame.font.SysFont(None, 36)
    texts = [
    font.render("1 - Graveyard", True, (255, 255, 255)),
    font.render("2 - Haunted House", True, (255, 255, 255)),
    font.render("3 - Forest", True, (255, 255, 255)),
    font.render("4 - Pumpkin Patch", True, (255, 255, 255))
    ]
    for i, text in enumerate(texts):
        match i:
            case 0:
                screen.blit(text, (WIDTH/4 - 60, HEIGHT/4))
            case 1:
                screen.blit(text, (WIDTH*0.75 - 90, HEIGHT/4))
            case 2:
                screen.blit(text, (WIDTH/4 - 50, HEIGHT*0.75))
            case 3:
                screen.blit(text, (WIDTH*0.75 - 90, HEIGHT*0.75))

    clock.tick(6)

    if rounds >= 10:
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"Final Score: {score}/10", True, (255, 255, 255)), (WIDTH/2, HEIGHT/2))
    
    pygame.display.flip()

pygame.quit()

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


class GameManager:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.game_ended = False
        self.current_state = 1
        self.next_state = random.choices(range(4), weights = transition_matrix[self.current_state], k = 1)[0]
    def check_guess(self, decision):
        self.rounds += 1
        if self.current_state == decision:
            self.current_state = self.next_state
            self.next_state = random.choices(range(4), weights = transition_matrix[self.current_state], k = 1)[0]
            self.score += 1
            print(f"Correct! Score: {self.score}")
        else:
            print(f"The monster escaped! Score: {self.score}")
            self.current_state = self.next_state
            self.next_state = random.choices(range(4), weights = transition_matrix[self.current_state], k = 1)[0]
            

manager = GameManager()

rewards = [10, 5, 8, 20]
exp = []
for i in range(4):
    value = transition_matrix[manager.current_state][i]
    exp.append(value)
best = exp.index(max(exp))

ambush_decision = 0
gameloop = True
while gameloop:
    print(best)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    keys = pygame.key.get_pressed()
    if not manager.game_ended:
        if keys[pygame.K_1]:
            ambush_decision = 0
            manager.check_guess(ambush_decision)
        elif keys[pygame.K_2]:
            ambush_decision = 1
            manager.check_guess(ambush_decision)
        elif keys[pygame.K_3]:
            ambush_decision = 2
            manager.check_guess(ambush_decision)
        elif keys[pygame.K_4]:
            ambush_decision = 3
            manager.check_guess(ambush_decision)
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

    clock.tick(10)

    if manager.rounds >= 10:
        screen.fill((0, 0, 0))
        screen.blit(font.render(f"Final Score: {manager.score}/10", True, (255, 255, 255)), (WIDTH/2 - 90, HEIGHT/2))
        manager.game_ended = True
    
    pygame.display.flip()

pygame.quit()

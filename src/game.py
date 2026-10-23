import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Zelda-style Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.player.update()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

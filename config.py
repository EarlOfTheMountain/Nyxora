# config.py
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TILE_SIZE = 32

# main.py
import pygame
from src.game import Game

pygame.init()
game = Game()
game.run()

# src/game.py
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

# src/player.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))  # Green square for now
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    
    def update(self):
        self.handle_input()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


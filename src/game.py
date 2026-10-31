import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.player import Player
from src.map import TileMap

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nyxora")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Load tilemap
        self.tilemap = TileMap("assets/maps/room_1.csv")
        
        # Create player (start in middle of first grass area)
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.player.set_tilemap(self.tilemap)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.player.update()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tilemap.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


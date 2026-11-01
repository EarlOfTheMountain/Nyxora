import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.player import Player
from src.room_manager import RoomManager

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nyxora")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Create room manager
        self.room_manager = RoomManager("room_1")
        
        # Create player
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.player.set_tilemap(self.room_manager.current_tilemap)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def check_room_transition(self):
        """Check if player has hit a door"""
        door = self.room_manager.current_tilemap.check_door_collision(self.player.rect)
        
        if door:
            # Determine which room to go to
            # For now, just toggle between room_1 and room_2
            next_room = "room_2" if self.room_manager.current_room_name == "room_1" else "room_1"
            
            # Get spawn position in next room (opposite side)
            spawn_x, spawn_y = self.room_manager.get_opposite_door(
                self.room_manager.current_room_name
            )
            
            # Transition
            self.room_manager.transition_to_room(next_room, spawn_x, spawn_y)
            self.player.set_tilemap(self.room_manager.current_tilemap)
            self.player.rect.center = (spawn_x, spawn_y)
            print(f"Entered {next_room}!")
    
    def update(self):
        self.player.update()
        self.check_room_transition()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.room_manager.current_tilemap.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


import pygame
import csv
from config import TILE_SIZE

class Tile(pygame.sprite.Sprite):
    """Individual tile sprite"""
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.tile_type = tile_type  # 0 = grass, 1 = wall, 2 = door
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        
        # Color based on tile type
        if tile_type == 0:  # Grass
            self.image.fill((34, 139, 34))  # Forest green
        elif tile_type == 1:  # Wall
            self.image.fill((101, 67, 33))  # Brown
        elif tile_type == 2:  # Door
            self.image.fill((255, 215, 0))  # Gold
        
        self.rect = self.image.get_rect(topleft=(x, y))

class TileMap:
    """Loads and manages the tilemap"""
    def __init__(self, csv_path):
        self.tiles = []
        self.collision_rects = []
        self.doors = []  # List of door rects
        self.load_map(csv_path)
    
    def load_map(self, csv_path):
        """Load map from CSV file"""
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            for row_idx, row in enumerate(reader):
                for col_idx, tile_type in enumerate(row):
                    tile_type = int(tile_type)
                    x = col_idx * TILE_SIZE
                    y = row_idx * TILE_SIZE
                    
                    tile = Tile(x, y, tile_type)
                    self.tiles.append(tile)
                    
                    # Walls are collidable
                    if tile_type == 1:
                        self.collision_rects.append(tile.rect)
                    # Doors are interactive
                    elif tile_type == 2:
                        self.doors.append(tile.rect)
    
    def draw(self, surface):
        """Draw all tiles"""
        for tile in self.tiles:
            surface.blit(tile.image, tile.rect)
    
    def check_collision(self, rect):
        """Check if rect collides with any wall tile"""
        for wall_rect in self.collision_rects:
            if rect.colliderect(wall_rect):
                return True
        return False
    
    def check_door_collision(self, rect):
        """Check if rect collides with a door and return it"""
        for door_rect in self.doors:
            if rect.colliderect(door_rect):
                return door_rect
        return None


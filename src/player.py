import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))  # Green square for now
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.tilemap = None  # Will be set by game
    
    def set_tilemap(self, tilemap):
        """Set reference to tilemap for collision detection"""
        self.tilemap = tilemap
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        
        # Move and check collision
        self.rect.x += dx
        if self.tilemap and self.tilemap.check_collision(self.rect):
            self.rect.x -= dx  # Undo x movement
        
        self.rect.y += dy
        if self.tilemap and self.tilemap.check_collision(self.rect):
            self.rect.y -= dy  # Undo y movement
    
    def update(self):
        self.handle_input()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


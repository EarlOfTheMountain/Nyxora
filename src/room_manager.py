from src.map import TileMap
from config import TILE_SIZE

class RoomManager:
    """Manages rooms and transitions between them"""
    
    # Define the world structure: which rooms connect to which
    WORLD = {
        "room_1": {
            "path": "assets/maps/room_1.csv",
            "exits": {
                # When player hits door in room_1, go to room_2
                # We'll use door index (0 = first door, etc.)
            }
        },
        "room_2": {
            "path": "assets/maps/room_2.csv",
            "exits": {}
        }
    }
    
    def __init__(self, starting_room="room_1"):
        self.current_room_name = starting_room
        self.current_tilemap = self._load_room(starting_room)
        self.player_spawn_pos = {}  # Track where player should spawn in each room
    
    def _load_room(self, room_name):
        """Load a room's tilemap"""
        if room_name not in self.WORLD:
            print(f"Room {room_name} not found!")
            return None
        
        path = self.WORLD[room_name]["path"]
        return TileMap(path)
    
    def transition_to_room(self, room_name, player_spawn_x, player_spawn_y):
        """Change to a different room and return the new tilemap"""
        if room_name not in self.WORLD:
            print(f"Room {room_name} not found!")
            return None
        
        self.current_room_name = room_name
        self.current_tilemap = self._load_room(room_name)
        self.player_spawn_pos[room_name] = (player_spawn_x, player_spawn_y)
        return self.current_tilemap
    
    def get_opposite_door(self, current_room, door_index=0):
        """
        Get the spawn position in the next room.
        For simplicity, we'll just use the opposite side of the next room.
        """
        # This is a simple implementation - customize as needed
        spawn_x = TILE_SIZE * 12  # Middle-ish of map
        spawn_y = TILE_SIZE * 2   # Top area
        return spawn_x, spawn_y


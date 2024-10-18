class Segment():
    # Holds data for a single segment
    def __init__(self, seg_no, position, char, is_head=False):
        # Initialise class variables
        self._size = 30
        self._speed = self._size + 5
        self._seg_no = seg_no
        self._pos_x = position[0]
        self._pos_y = position[1]
        self._velocity_x = None
        self._velocity_y = None
        self._char = char

        # Set initial position and speed for the head segment
        if is_head:
            self._velocity_x = self._speed
            self._velocity_y = 0
            
        # Used to pass information onto the next segment in the list
        self._old_velocity_x = None
        self._old_velocity_y = None

    def move(self):
        # Move segment based on current velocity
        self._pos_x += self._velocity_x
        self._pos_y += self._velocity_y
        self._old_velocity_x = self._velocity_x
        self._old_velocity_y = self._velocity_y

    def turn(self, direction):
        # Update segment velocity providing it is not opposite to current velocity
        # Only used by head segment
        if (direction[0] != 0 and self._velocity_x != 0) or (direction[1] != 0 and self._velocity_y != 0):
            pass
        else:
            self._velocity_x = direction[0] * self._speed
            self._velocity_y = direction[1] * self._speed

    def follow(self, velocity):
        # Update segment velocity based on proceeding segment
        # Only used by tail segments
        self._velocity_x = velocity[0]
        self._velocity_y = velocity[1]

    def get_rect(self):
        return self._pos_x - self._size / 2, self._pos_y - self._size / 2, self._size, self._size
    
    def get_pos(self):
        return self._pos_x, self._pos_y
    
    def get_vel(self):
        return self._velocity_x, self._velocity_y

    def echo(self):
        # Returns the old velocity values
        return self._old_velocity_x, self._old_velocity_y

    def get_char(self):
        return self._char
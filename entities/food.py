import random

class Food():
    
    def __init__(self, char, player):
        self._char = char
        self._pos = None
        self._size = 30
        self._char = char

        select_pos = True
        while select_pos:
            invalid = False
            self._pos_x = random.randrange(12, 702, 35) + 0.5
            self._pos_y = random.randrange(12, 702, 35) + 0.5
            counter = 0
            while counter < len(player):
                seg_pos = player[counter].get_pos()
                seg_vel = player[counter].get_vel()
                if seg_pos[0] == self._pos_x and seg_pos[1] == self._pos_y:
                    counter = len(player)
                    invalid = True
                else:
                    counter += 1
            if not invalid:
                select_pos = False

    def get_rect(self):
        return self._pos_x - self._size / 2, self._pos_y - self._size / 2, self._size, self._size
    
    def get_char(self):
        return self._char
    
    def get_pos(self):
        return self._pos_x, self._pos_y
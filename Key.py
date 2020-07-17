class Key:

    def __init__(self, key_val, key_state):
        self.key_val = key_val
        self.key_state = key_state

    def set_down(self):
        self.key_state = self.KeyState.DOWN

    def set_up(self):
        self.key_state = self.KeyState.UP

    def set_neutral(self):
        self.key_state = self.KeyState.NEUTRAL

    def is_down(self):
        if self.key_state == self.KeyState.DOWN:
            return True
        return False

    def is_up(self):
        if self.key_state == self.KeyState.UP:
            return True
        return False

    def is_neutral(self):
        if self.key_state == self.KeyState.NEUTRAL:
            return True
        return False

    class KeyState:
        DOWN = 0
        UP = 1
        NEUTRAL = 2

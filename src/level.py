class Level:


    def __init__(self):

        self.current = 1


    def increase(self):

        self.current += 1


    def enemy_count(self):
        
        return min(self.current, 3)
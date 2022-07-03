
class Player:
    """A sample Player class"""

    def __init__(self, name, score):
        self.name = name
        self.score = score
    

    def __repr__(self):
        return "player('{}', {})".format(self.name, self.score)
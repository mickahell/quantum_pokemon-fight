class Player:
    """Class of player :
    - name
    - status (J1 // J2)
    - being
    - action
    - pokemon
    - team
    - register_team"""

    def __init__(self, name, status, being):
        self.name = name
        self.status = status
        self.being = being
        self.action = 0
        self.team = []
        self.register_team = []

    def addFirst(self, pokemon):
        self.pokemon = pokemon

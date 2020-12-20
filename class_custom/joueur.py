class Joueur:
    """Classe définissant un joueur :
    - nom
    - status (J1 // J2)
    - action
    - pokemon
    - team"""

    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.action = 0
        self.team = []

    def addFirst(self, pokemon):
        self.pokemon = pokemon


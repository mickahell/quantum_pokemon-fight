class Joueur:
    """Classe définissant un joueur :
    - nom
    - status (J1 // J2)
    - action
    - pokemon"""

    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.action = 0 

    def addEquipe(self, pokemon):
        self.pokemon = pokemon


class Attaque:
    """Classe définissant une personne caractérisée par :
    - nom
    - type
    - puissance
    - précision"""

    def __init__(self, nom, type, puissance, precision, status):
        self.nom = nom
        self.type = type
        self.puissance = puissance
        self.precision = precision
        self.status = status

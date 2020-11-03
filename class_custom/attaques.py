class Attaque:
    """Classe définissant une capacité (attaque) :
    - nom
    - type
    - puissance
    - précision"""

    def __init__(self, nom, type, puissance, precision, status):
        self.name = nom
        self.type = type
        self.puissance = puissance
        self.precision = precision
        self.status = status

class Pokemon:
    """Classe définissant une personne caractérisée par :
    - nom
    - stats (pv // att // def // sp_att // sp_def // vitesse)
    - type(s)
    - attaques []
    - status (vie // mort)
    - dégats
    - aski (j1 // j2)"""

    pokedex = [] # nb de pokemon crée
    def __init__(self, name, types, pv, points_attaque, points_defence, points_att_sp, points_def_sp, vitesse):
        self.name = name
        self.types = types
        self.pv = pv
        self.points_attaque = points_attaque
        self.points_defence = points_defence
        self.points_att_sp = points_att_sp
        self.points_def_sp = points_def_sp
        self.vitesse = vitesse
        self.status = 1
        self.degats = 0
        self.attaques = []

        Pokemon.pokedex.append(self)

    def apprendre_attaques(self, attaques):
        self.attaques = attaques

    def show_info(self):
        print("{}, {} | {} pv, {} att, {} def, {} attSP, {} defSP, {} vitesse".format(self.name, self.types,
                                                                                      self.pv, self.points_attaque,
                                                                                      self.points_defence,
                                                                                      self.points_att_sp,
                                                                                      self.points_def_sp, self.vitesse))
        print("Attaques : {}".format(self.attaques))

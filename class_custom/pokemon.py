class Pokemon:
    """Class of pokemon :
    - name
    - stats (pv // att // def // sp_att // sp_def // speed)
    - type(s)
    - attacks []
    - status (alive // dead)
    - dommages
    - aski (j1 // j2)
    - malus (burn, freeze, poison, paralysis, none)"""

    pokedex = [] # nb of pokemon making
    def __init__(self, name, types, pv, points_attack, points_defense, points_att_sp, points_def_sp, speed):
        self.name = name
        self.types = types
        self.pv = pv
        self.points_attack = points_attack
        self.points_defense = points_defense
        self.points_att_sp = points_att_sp
        self.points_def_sp = points_def_sp
        self.speed = speed
        self.status = 1
        self.dommages = 0
        self.attacks = []
        self.malus = "None"

        Pokemon.pokedex.append(self)

    def learn_attacks(self, attacks):
        self.attacks = attacks

    def show_info(self):
        print("{}, {} | {} pv, {} att, {} def, {} attSP, {} defSP, {} speed".format(self.name, self.types,
                                                                                      self.pv, self.points_attack,
                                                                                      self.points_defense,
                                                                                      self.points_att_sp,
                                                                                      self.points_def_sp, self.speed))
        print("Attacks : {}".format(self.attacks))

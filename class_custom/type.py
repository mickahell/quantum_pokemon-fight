class Type:
    """Classe définissant un type :
    - nom
    - résistance []
    - faiblesse []
    - imunite []
    - qubit """

    def __init__(self, name):
        self.name = name
        self.resistance = []
        self.faiblesse = []
        self.imunite = []
        self.qubit = name

    def add_info(self, resistance, faiblesse, immunite):
        self.resistance = resistance
        self.faiblesse = faiblesse
        self.imunite = immunite

    def show_info(self):
        if self.imunite:
            print("{} | Résistance : {}, Faiblesse : {}, Imunité : {}".format(
                self.name, self.resistance, self.faiblesse, self.imunite))
        else:
            print("{} | Résistance : {}, Faiblesse : {}".format(
                self.name, self.resistance, self.faiblesse))

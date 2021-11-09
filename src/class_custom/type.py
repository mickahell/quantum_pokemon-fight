class Type:
    """Class of type :
    - name
    - résistance []
    - weakness []
    - imunite []
    - qubit """

    def __init__(self, name):
        self.name = name
        self.resistance = []
        self.weakness = []
        self.imunite = []
        self.qubit = name

    def add_info(self, resistance, weakness, immunite):
        self.resistance = resistance
        self.weakness = weakness
        self.imunite = immunite

    def show_info(self):
        if self.imunite:
            print("{} | Resistance : {}, Weakness : {}, Imunity : {}".format(
                self.name, self.resistance, self.weakness, self.imunite))
        else:
            print("{} | Resistance : {}, Weakness : {}".format(
                self.name, self.resistance, self.weakness))

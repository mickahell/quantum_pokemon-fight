class Attack:
    """Class of move (attack) :
    - name
    - type
    - power
    - precision"""

    def __init__(self, name, type, power, precision, status):
        self.name = name
        self.type = type
        self.power = power
        self.precision = precision
        self.status = status

class Type: # Définition de notre classe Personne
  """Classe définissant une personne caractérisée par :
  - nom
  - résistance
  - faiblesse"""
  
  def __init__(self, nom, resistance, faiblesse): # Notre méthode constructeur
    self.nom = nom
    self.resistance = resistance
    self.faiblesse = faiblesse

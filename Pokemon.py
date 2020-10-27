class Pokemon: # Définition de notre classe Personne
  """Classe définissant une personne caractérisée par :
  - nom
  - stats (pv // att // def // sp_att // sp_def // vitesse)
  - type(s)
  - attaques
  - status (vie // mort)
  - dégats
  - aski (j1 // j2)"""
  
  def __init__(self, nom, stats, types, attaques): # Notre méthode constructeur
    """Pour l'instant, on ne va définir qu'un seul attribut"""
    self.nom = nom
    self.types = types
    self.attaques = attaques
   
  def __init__(self, pv, points_attaque, points_defence, points_att_sp, points_def_sp, vitesse):
    self.pv = pv
    self.points_attaque = points_attaque
    self.points_defence = points_defence
    self.points_att_sp = points_att_sp
    self.points_def_sp = points_def_sp
    self.vitesse = vitesse
    

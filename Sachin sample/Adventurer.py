#Sample class for sample.py
class Adventurer:
  def __init__(self, health=100, strength=None, dexterity=None, intellect=None, 
  endurance=None, charisma=None, luck=5):
    self.health = health
    self.strength = strength
    self.dexterity = dexterity
    self.intellect = intellect
    self.endurance = endurance
    self.charisma = charisma
    self.luck = luck

  def setStrength(self,str):
    self.strength=str

  def takeDamage(self,damage):
    self.health = self.health - damage

  def attack(self,type):
    damage = 0
    if(type == "meele"):
      damage = self.strength*2
    return damage
    
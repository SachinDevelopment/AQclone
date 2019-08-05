import Adventurer
import constant

sachin = Adventurer.Adventurer()
parth = Adventurer.Adventurer()
sachin.setStrength(10)
parth.setStrength(20)


print(sachin.health)
print(sachin.takeDamage(parth.attack(constant.MEELE)))
print(sachin.health)

print(parth.health)
print(parth.takeDamage(sachin.attack(constant.MEELE)))
print(parth.health)
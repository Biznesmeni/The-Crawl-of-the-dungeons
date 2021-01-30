
from EquipmentVariables import *
from PlayerVariables import *


if ArmorLight == True:
    PlayerDefense=1 + DefenseModifier 
    
if ArmorHeavy == True: 
    PlayerDefense=2 + DefenseModifier 
        
if Sword == True:
    PlayerDamage=4 + AttackModifier
 

if Staff == True:
    PlayerManaMax=10 + ManaModifier
    
if Axe == True:
    PlayerDamage=5 + AttackModifier
 
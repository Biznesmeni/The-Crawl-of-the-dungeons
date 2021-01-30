
from ItemsWhenEquipped import *
from PlayerVariables import *
from EquipmentVariables import *


if ArmorLight == True:
    PlayerDefense=1 + DefenseModifier 
    
if ArmorHeavy == True: 
    PlayerDefense=2 + DefenseModifier 
        
if Sword == True:
    PlayerDamage=4 + AttackModifier
    CanCastSpell = False
 

if Staff == True:
    PlayerManaMax=10 + ManaModifier
    CanCastSpell = True
    
if Axe == True:
    PlayerDamage=5 + AttackModifier
    CanCastSpell = False

 
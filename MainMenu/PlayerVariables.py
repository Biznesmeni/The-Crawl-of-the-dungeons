import pygame


ClassDruid=False
ClassBarbarian=False
ClassHunter=False

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')

char = pygame.image.load('standing.png')

class Player():
    def __init__(self, name, HP, damage, ):
        self.name = name
        self.HP = HP
        self.damage = damage
    
    def IncreaseHP(self, NewHP):
        self.HP = NewHP
        
    
if ClassDruid == True:
    PlayerManaMax = 20
    PlayerManaCurrent = 20
    PlayerHealthMax = 8
    PlayerHealthCurrent = 8
    PlayerHealthMax = 14
    PlayerHealthCurrent = 14
    PlayerDamage = 2
    Staff = True
    PlayerDodgechance = 5
    PlayerHitChance = 70
    
if ClassBarbarian == True:
    PlayerhealthMax = 25
    PlayerHealthCurrent = 25
    PlayerManaMax = 0
    PlayerManaCurrent = 0
    PlayerDamage = 5
    PlayerDodgeChance = 5
    PlayerHitChance = 65
    Axe=True
    ArmorHeavy=True
    
if ClassHunter == True:
    PlayerManaMax = 10
    PlayerManaCurrent = 10
    PlayerHealthMax = 20
    PlayerHealthCurrent = 20
    PlayerDamage = 0
    Bow = True
    Sword = True
    PlayerDodgechance = 20
    PlayerHitChance = 80

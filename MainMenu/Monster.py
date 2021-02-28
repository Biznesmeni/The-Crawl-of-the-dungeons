import pygame



class Monster():
    Monster = ('Alive')
    def monsterHP(self, MonsterHP):
        self.MonsterHP = MonsterHP
        if self.MonsterHP == 0:
            Monster = ('Dead')
    def monsterType(self, MonsterType, Damage):
        self.MonsterType = MonsterType
        self.Damage = Damage
        if MonsterType == ('Fire'):  
            if WeaponElement == WaterDamage:  
                self.Damage = self.Damage*3
        if MonsterType == ('Ice'):
            if WeaponElement == FireDamage:
                self.Damage = self.Damage*3
        if MonsterType == ('Water'):
            if WeaponElement == IceDamage:
                self.Damage = self.Damage*3
        if MonsterType == ('Earth'):
            if WeaponElement == NormalDamage:
                self.Damage = self.Damage*3
        if MonsterType == ('Necromancy'):
             if WeaponElement == HolyDamage:
                self.Damage = self.Damage*3
        if MonsterType == ('Normal'):
            Damage = Damage
    def monsterSpeed(self, MonsterSpeed):
        self.MonsterSpeed = MonsterSpeed
    def monsterAttack(self, MonsterAttack, MonsterImg):
        self.MonsterAttack = MonsterAttack

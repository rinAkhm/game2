# from abc import ABC, abstractmethod
import random


#
#
# class ClassHeroInGame:
#     def __init__(self, name, ):
#
#
#     @abstractmethod
#     def skill(self, enemy):
#         pass
#
#
# class ClassWarrior(ClassHeroInGame):
#     def skill(self, enemy):
#         if enemy == 'meelle':
#             armor_skill = random.randit(1, 15)
#             return armor_skill
#         else:
#             return 0
#
#
# class ClassMage:
#     def skill(self, enemy):
#         if enemy == 'spell_shot':
#             armor_skill = random.randint(1, 15)
#             return armor_skill
#         else:
#             return 0
#
#
# class ClassHanter:
#     def skill(self, enemy):
#         if enemy == 'long_shot':
#             armor_skill = random.randint(1, 15)
#             return armor_skill
#         else:
#             return 0

class Manager:
    __hero = None

    def setHero(self, hero):
        self.__hero = hero

    def get_items(self):
        item = Item()

        name = self.__hero.getName()
        item.setName(name)

        weapon = self.__hero.getWeapon()
        item.setWeapon(weapon)

        attack = self.__hero.getAttack()
        item.setAttack(attack)

        hp = self.__hero.getHp()
        item.setHp(hp)
        return item

class Item:
    def __init__(self):
        self.__name = None
        self.__weapon = None
        self.__attack = None
        self.__hp = None

    def setName(self, name):
        self.__name = name

    def setWeapon(self, weapon):
        self.__weapon = weapon

    def setAttack(self, attack):
        self.__attack = attack

    def setHp(self, hp):
        self.__hp = hp

    def state(self):
        print (f'Герой {self.__name.name} ({self.__hp.hp} жизней) - оружие {self.__weapon.item} ({self.__attack.attack} атака)')


class Creator:
    def getName(self,nickname): pass

    def getWeapon(self, weapon): pass

    def getAttack(self, attack): pass

    def getHp(self, count_hp): pass


class CreaterHero(Creator):

    def getName(self):
        name = Name()
        name.name = 'Rinat'
        return name

    def getWeapon(self):
        item = Weapon()
        item.item = 'rapier'
        return item

    def getAttack(self):
        attack = Attack()
        attack.attack = 10
        return attack

    def getHp(self):
        hp = Hp()
        hp.hp = 10
        return hp


class Name:
    name = None


class Weapon:
    item = None


class Attack:
    attack = None


class Hp:
    hp = None


hero_game = CreaterHero()
# hero_game.getAttack(10)
# hero_game.getHp(10)
# hero_game.getName('Rinat')
# hero_game.getWeapon('rapier')

manager = Manager()

manager.setHero(hero_game)
hero = manager.get_items()
hero.state()
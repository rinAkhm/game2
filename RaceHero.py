from abc import ABC, abstractmethod
from Items import Manager
import random


class ObjectRace(ABC):

    @abstractmethod
    def get_skill(self):
        pass

    @abstractmethod
    def choice_race(self):
        pass

    @abstractmethod
    def improve_weapon(self):
        pass


class Warrior(ObjectRace):
    def get_skill(self, enemy):
        skill = [True, False]
        if enemy == 'meelle':
            dodge = random.choice(skill)
            return dodge
        else:
            return 0

    def choice_race(self):
        return 'Warrior'

    def improve_weapon(self, race, weapon):
        if race == f'{self.choice_race()}' and weapon.get('rapier', False):
            weapon['rapier'] += 5
            return weapon
        else:
            return 0


class Mage(ObjectRace):
    def get_skill(self, enemy):
        skill = [True, False]
        if enemy == 'spell_shot':
            dodge = random.choice(skill)
            return dodge
        else:
            return 0

    def choice_race(self):
        return 'Mage'

    def improve_weapon(self, race, weapon):
        if race == f'{self.choice_race()}' and weapon.get('magic_book', False):
            weapon['magic_book'] += 5
            return weapon
        else:
            return 0


class Hunter(ObjectRace):
    def get_skill(self, enemy):
        skill = [True, False]
        if enemy == 'long_shot':
            dodge = random.choice(skill)
            return dodge

    def choice_race(self):
        return 'Hunter'

    def improve_weapon(self, race, weapon):
        if race == f'{self.choice_race()}' and weapon == 'bow':
            weapon += 5
            return weapon
        else:
            return 0


class RaceFactory(ABC):
    @abstractmethod
    def create_race(self):
        pass


class WarriorFactory(RaceFactory):
    def create_race(self):
        return Warrior()


class MageFactory(RaceFactory):
    def create_race(self):
        return Mage()


class HunterFactory(RaceFactory):
    def create_race(self):
        return Hunter()


class ManagerRace:
    def get_race(self, race):
        spawner_to_factory_mapping = {
            "Warrior": WarriorFactory,
            "Mage": MageFactory,
            "Hunter": HunterFactory
        }

        spawner = spawner_to_factory_mapping[race]()
        enemy = spawner.create_enemy()
        action = enemy.damage()
        return action


# boy = WarriorFactory()
# action = boy.create_race()
# print(action.choice_race())
# action.get_skill('meelle')
# action.improve_weapon(action.choice_race(), {'rapier': 15})
#
# her = Hero(name="Rinat", race=action.choice_race(), weapon={'rarpier': 15})
# print(her)

#
# class temp(Hero, ObjectRace):
#     pass
#
#     def get_race(self, race):
#         self.race = {}
#         if race == 1:
#             race_skill = random.randint(1, 10)
#             race_skill['Warrior'] = race_skill
#             return race_skill
#
#         elif self.race == 2:
#             race_skill = random.randint(1, 10)
#             race_skill['Mage'] = race_skill
#             return race_skill
#
#         elif self.race == 3:
#             race_skill = random.randint(1, 10)
#             race_skill['Hunter'] = race_skill
#             return race_skill
#
#     def choice_race(self):
#         while True:
#             try:
#                 race = int(input("Выберите расу:\n"
#                                  "1. Warrior\n"
#                                  "2. Mage\n"
#                                  "3. Hunter\n"))
#             except TypeError:
#                 raise ('Ошибка ввода, попробуй ввести еще раз')
#                 continue
#             if race == 1 or race == 2 or race == 3:
#                 self.get_race(race)
#                 return
#
#
# per = Hero()

from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Абстрактный класс игрового противника."""
    monster_hp = None
    monster_attack = None
    type_damage = None

    @abstractmethod
    def damage(self):
        """Метод атаки."""
        pass


class Ogre(Enemy):

    def damage(self):
        print('Огр бежит в атаку')
        Enemy.monster_hp = random.randint(6, 10)
        Enemy.monster_attack = random.randint(6, 10)
        Enemy.type_damage = 'physical_attack'
        return Enemy.type_damage, Enemy.monster_hp, Enemy.monster_attack


class Skeleton(Enemy):

    def damage(self):
        print('Скелет стреляет стрелами')
        Enemy.monster_hp = random.randint(6, 10)
        Enemy.monster_attack = random.randint(6, 10)
        Enemy.type_damage = 'physical_attack'
        return Enemy.type_damage, Enemy.monster_hp, Enemy.monster_attack

class Goblin(Enemy):
    def damage(self):
        print('Гоблин пускает огненные шары')
        Enemy.monster_hp = random.randint(6, 10)
        Enemy.monster_attack = random.randint(6, 10)
        Enemy.type_damage = 'physical_attack'
        return Enemy.type_damage, Enemy.monster_hp, Enemy.monster_attack

class EnemyFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта."""
        pass


class OgreFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return Ogre()


class SkeletonFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return Skeleton()


class GoblinFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self):
        return Goblin()


spawner_to_factory_mapping = {
    "ogre": OgreFactory,
    "skeleton": SkeletonFactory,
    "goblin": GoblinFactory
}

# enemy_type_list = ["ogre", "skeleton", "goblin"]
#
# for i in range(10):create_enemy
#     SPAWNER_TYPE = random.choice(enemy_type_list)
#
#     spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
#
#     enemy = spawner.create_enemy()
#     action = enemy.damage()
#     print(action)

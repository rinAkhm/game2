from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Абстрактный класс игрового противника."""

    @abstractmethod
    def damage(self):
        """Метод атаки."""
        pass


class Ogre(Enemy):

    def damage(self):
        indicators = dict()
        indicators['name'] = 'Орк'
        indicators['type_damage'] = 'mellee'
        indicators['attack'] = random.randint(6, 10)
        indicators['hp'] = random.randint(6, 10)
        return indicators


class Skeleton(Enemy):

    def damage(self):
        indicators = dict()
        indicators['name'] = 'Скелет'
        indicators['type_damage'] = 'long_shot'
        indicators['attack'] = random.randint(6, 10)
        indicators['hp'] = random.randint(6, 10)
        return indicators


class Goblin(Enemy):
    def damage(self):
        indicators = dict()
        indicators['name'] = 'Гоблин'
        indicators['type_damage'] = 'spell_shot'
        indicators['attack'] = random.randint(6, 10)
        indicators['hp'] = random.randint(6, 10)
        return indicators


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


class SpanEnemy:
    @property
    def get_monster(self):
        spawner_to_factory_mapping = {
            "ogre": OgreFactory,
            "skeleton": SkeletonFactory,
            "goblin": GoblinFactory
        }

        enemy_type_list = ["ogre", "skeleton", "goblin"]
        SPAWNER_TYPE = random.choice(enemy_type_list)
        spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
        enemy = spawner.create_enemy()
        action = enemy.damage()
        return action

if __name__ == '__main__':
    span = SpanEnemy()
    print(span.get_monster)
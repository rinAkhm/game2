from abc import ABC, abstractmethod
import random


class ObjectGame(ABC):
    """Абстрактный класс игрового предмета."""
    apple = None
    rapier = None
    totem = None
    bow = None
    magic_book = None
    arrows = None

    @abstractmethod
    def item(self):
        """Свойства предмета."""
        pass


class Apple(ObjectGame):
    def item(self):
        ObjectGame.apple = random.randint(6, 15)
        print(f'Нашли хилл на {ObjectGame.apple} хп')
        return ObjectGame.apple


class Rapier(ObjectGame):
    def item(self):
        ObjectGame.rapier = random.randint(10, 20)
        print(f'Нашли меч c атакой {ObjectGame.rapier}')
        return ObjectGame.rapier


class Bow(ObjectGame):
    def item(self):
        ObjectGame.bow = random.randint(10, 20)
        print(f'Нашли лук c атакой {ObjectGame.bow}')
        return ObjectGame.bow


class Arrows(ObjectGame):
    def item(self):
        ObjectGame.arrows = 15
        print(f'Нашли стрелы {ObjectGame.arrows} штук')
        return ObjectGame.arrows


class MagicBook(ObjectGame):
    def item(self):
        ObjectGame.magic_book = random.randint(10, 20)
        print(f'Нашли магическую книгу с {ObjectGame.magic_book} атакой')
        return ObjectGame.magic_book


class Totem(ObjectGame):
    def item(self):
        ObjectGame.totem = 'Тотем'
        print(f'Нашли тотем')
        return ObjectGame.totem


class ObjectFactory(ABC):
    """Абстрактная фабрика игрового предмета."""

    @abstractmethod
    def create_item(self):
        """Создание абстрактного предмета."""
        pass


class AppleFactory(ObjectFactory):
    """Конкретная фабрика игрового яблока."""

    def create_item(self):
        return Apple()


class RapierFactory(ObjectFactory):
    """Конкретная фабрика игрового меча."""

    def create_item(self):
        return Rapier()


class BowFactory(ObjectFactory):
    """Конкретная фабрика игрового лука."""

    def create_item(self):
        return Bow()


class ArrowsFactory(ObjectFactory):
    """Конкретная фабрика игровых стрел."""

    def create_item(self):
        return Arrows()


class MagicBookFactory(ObjectFactory):
    """Конкретная фабрика игровой магической книги."""

    def create_item(self):
        return MagicBook()


class TotemFactory(ObjectFactory):
    """Конкретная фабрика игрового тотема."""

    def create_item(self):
        return Totem()


def get_item():
    spawner_to_factory_mapping = {
        "apple": ArrowsFactory,
        "rapier": RapierFactory,
        "bow": BowFactory,
        "arrows": ArrowsFactory,
        "magic_book": MagicBookFactory,
        "totem": TotemFactory
    }

    item_type_list = ["apple", "rapier", "bow", "arrows", "magic_book", "totem"]
    SPAWNER_TYPE = random.choice(item_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    object = spawner.create_item()
    action = object.item()
    return action


if __name__ == '__main__':
    get_item()

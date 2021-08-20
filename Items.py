"""Фабричная фабрика по созданию вещей."""

from abc import ABC, abstractmethod
import random


class ObjectGame(ABC):
    """Абстрактный класс игрового предмета."""

    @abstractmethod
    def item(self) -> dict:
        """Свойства предмета."""
        pass


class Apple(ObjectGame):
    """Абстрактная фабрика яблок."""

    def item(self) -> dict:
        """Свойстсва яблока."""
        apple = dict()
        apple["apple"] = random.randint(6, 15)
        return apple


class Rapier(ObjectGame):
    """Абстрактная фабрика мечей."""

    def item(self) -> dict:
        """Свойстсва меча."""
        weapon = dict()
        weapon["rapier"] = random.randint(10, 20)
        return weapon


class Bow(ObjectGame):
    """Абстрактная фабрика луков."""

    def item(self) -> dict:
        """Свойстсва лука."""
        bow = dict()
        bow["bow"] = random.randint(10, 20)
        return bow


class Arrows(ObjectGame):
    """Абстрактная фабрика стрел."""

    def item(self) -> dict:
        """Свойстсва стрел."""
        arrows = dict()
        arrows["arrows"] = random.randint(5, 15)
        return arrows


class MagicBook(ObjectGame):
    """Абстрактная фабрика магических книг."""

    def item(self) -> dict:
        """Свойстсва магической книги."""
        magic_book = dict()
        magic_book["magic_book"] = random.randint(10, 20)
        return magic_book


class Totem(ObjectGame):
    """Абстрактная фабрика тотемов."""

    def item(self) -> dict:
        """Свойстсва тотема."""
        totem = dict()
        totem["totem"] = True
        return totem


class ObjectFactory(ABC):
    """Абстрактная фабрика игрового предмета."""

    @abstractmethod
    def create_item(self) -> object:
        """Создание абстрактного предмета."""
        pass


class AppleFactory(ObjectFactory):
    """Конкретная фабрика игрового яблока."""

    def create_item(self) -> Apple:
        """Создает яблоко."""
        return Apple()


class RapierFactory(ObjectFactory):
    """Конкретная фабрика игрового меча."""

    def create_item(self) -> Rapier:
        """Создает меч."""
        return Rapier()


class BowFactory(ObjectFactory):
    """Конкретная фабрика игрового лука."""

    def create_item(self) -> Bow:
        """Создает лук."""
        return Bow()


class ArrowsFactory(ObjectFactory):
    """Конкретная фабрика игровых стрел."""

    def create_item(self) -> Arrows:
        """Создает стрелы."""
        return Arrows()


class MagicBookFactory(ObjectFactory):
    """Конкретная фабрика игровой магической книги."""

    def create_item(self) -> MagicBook:
        """Создает магические книги."""
        return MagicBook()


class TotemFactory(ObjectFactory):
    """Конкретная фабрика игрового тотема."""

    def create_item(self) -> Totem:
        """Создает тотем."""
        return Totem()

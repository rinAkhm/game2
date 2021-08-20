"""Главный файл для запуска игры."""

from BasicHero import Hero
from BasicEvent import GenerateEvent

# from typing import Any
import sys

COUNT_MONSTERS = 0


def valid_number(number: str) -> str:
    """Проверка на ввод корректного числа."""
    while True:
        if number == "1" or number == "2":
            return number
        else:
            number = input("Для корректного ввода введите 1 или 2")


def valid_number2(number: str) -> str:
    """Проверка на ввод корректного числа."""
    while True:
        if number == "1" or number == "2" or number == "3":
            return number
        else:
            number = input(
                "Для корректного ввода введите\n "
                "\n1 - выбрать rapier"
                "\n2 - выбрать bow"
                "\n3 - выбрать magic book"
            )


def get_nickname() -> str:
    """Заполнение никнейма."""
    name = input("Введите пожалуйста свой никнейм: \n")
    return name


def battle(monster: dict, hero: Hero) -> bool:
    """Идет сражение."""
    global COUNT_MONSTERS
    name, damage, attack, hp_m = "", "", "", ""
    for key, value in monster.items():
        if key == "name":
            name = value
        elif key == "type_damage":
            damage = value
        elif key == "attack":
            attack = value
        else:
            hp_m = value

    print(f"\nБОЙ! Вы встрели монстра {name} {hp_m} хп {attack} дамаг")
    input_number = input("1 - Начать бой 2 - Убежать\n")
    input_number = valid_number(input_number)
    if input_number == "2":
        return True
    else:
        while hero.hp > 0 and hp_m > 0:
            weapon_attack = False
            improve_weapon = 0
            input_number = input("1 - Выбрать оружие 2 - Убежать\n")
            input_number = valid_number(input_number)
            if input_number == "2":
                return True
            else:
                while weapon_attack is False:
                    input_number_weapon = input(
                        f"\n1 - выбрать"
                        f" {hero.rapier}"
                        f"\n2 - выбрать {hero.bow} "
                        f"(стрел {hero.arrow})"
                        f"\n3 - выбрать "
                        f"{hero.magic_book}\n"
                    )
                    input_number_weapon = valid_number2(input_number_weapon)
                    weapon_attack = hero.get_attack_weapon(input_number_weapon)
                    if weapon_attack:
                        weapon_name = hero.get_name_weapon(input_number_weapon)
                        if weapon_name == "bow" and hero.arrow == 0:
                            print(
                                f"Количество стрел = {hero.arrow}, "
                                "вам нужно поменять оружение"
                            )
                            weapon_attack = False
                            continue
                        improve_weapon = hero.improve_weapon(weapon_name)
                    else:
                        print("Такого оружия у вас нет")
                        continue
                dodge = hero.dodge_attack(damage)
                if dodge:
                    hero.minus_hp(0)
                    hp_m = hp_m - (weapon_attack + improve_weapon)
                else:
                    hero.minus_hp(attack)
                    hp_m = hp_m - (weapon_attack + improve_weapon)
                if weapon_name == "bow":
                    hero.arrow -= 1
        if hero.hp > 0:
            COUNT_MONSTERS += 1
            print(f"Убито монстров {COUNT_MONSTERS}\n")
            return True
        else:
            if hero.totem:
                print("Вы проиграли бой")
                input_number = input("1 - Использовать тотем 2 - умереть\n")
                input_number = valid_number(input_number)
                if input_number == "1":
                    hero.name = hero.totem["nickname"]
                    hero.race = hero.totem["race"]
                    hero.hp = hero.totem["hp"]
                    hero.bow = hero.totem["bow"]
                    hero.magic_book = hero.totem["magic_book"]
                    hero.rapier = hero.totem["rapier"]
                    hero.arrow = hero.totem["arrows"]
                    hero.totem = None
                    print("Тотем сработал\n")
                    return True
                else:
                    return False
            else:
                return False


def choice_race() -> str:
    """Выбирает расу."""
    print("Введите число от 1 до 3 для выбора расы:")
    list_race = ["Warrior", "Mage", "Hunter"]
    while True:
        try:
            race = int(input("1. Warrior\n" "2. Mage\n" "3. Hunter\n"))
        except (ValueError):
            print("Нужно ввести число от 1-3 для выбора расы")
            continue
        if race in [1, 2, 3]:
            return list_race[race - 1]
        else:
            print("Нужно ввести число от 1-3 для выбора расы")


def get_item(action: dict, hero: Hero) -> bool:
    """Событие нахождения item."""
    for k, v in action.items():
        if k in ["rapier", "magic_book", "bow", "arrows"]:
            print(f"Вы нашли новый {k} {v} с атакой ")
            input_number = input(f"1 - Взять {k} c атакой {v}\n" f"2 - Пройти мимо\n")
            input_number = valid_number(input_number)
            if input_number == "1":
                if action.get("rapier", False):
                    hero.rapier = action
                    return True
                elif action.get("bow", False):
                    hero.bow = action
                    return True
                elif action.get("magic_book", False):
                    hero.magic_book = action
                    return True
                else:
                    hero.arrow += v
                    return True
            else:
                return False
        elif k in "apple":
            print(f"Вы нашли хил на {v}")
            hero.use_heal(v)
            return True
        else:
            input_number = input(f"Вы нашли {k}\n1 - Взять 2 - пройти мимо\n")
            input_number = valid_number(input_number)
            if input_number == "1":
                hero.totem = {"nickname": hero.name,
                              "hp": hero.hp,
                              "bow": hero.bow,
                              "rapier": hero.rapier,
                              "arrows": hero.arrow,
                              "magic_book": hero.magic_book,
                              "race": hero.race,
                            }
                return True
            else:
                return False


def game() -> None:
    """Происходит процесс игры."""
    name = get_nickname()
    race = choice_race()
    hero = Hero(name=name)
    class_race = hero.get_race(race)
    print(f"Персонаж создан {name} - {class_race} готов к великим сражениям!")
    while COUNT_MONSTERS < 10 and hero.hp > 0:
        event = GenerateEvent()
        action = event.get_event
        if action.get("name", False):
            fight = battle(action, hero)
            if fight:
                print(hero)
            else:
                print("Вы убежали\n")
                print(hero)
        else:
            get_item(action, hero)
    print("Победа")
    sys.exit()


if __name__ == "__main__":
    game()

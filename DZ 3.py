
ENEMY_DATA = [
    {"name": "Goblin", "health": 30, "attack": 5},
    {"name": "Orc", "health": 50, "attack": 10},
    {"name": "Dragon", "health": 100, "attack": 15}
]


class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack



hero = Hero("Knight", 150, 20)

print(f"Герой {hero.name} виходить на арену!")


for data in ENEMY_DATA:

    enemy = Enemy(**data)

    print(f"\nНа арену виходить {enemy.name}!")
    print(f"Здоров'я ворога: {enemy.health}")


    while hero.health > 0 and enemy.health > 0:


        enemy.health -= hero.attack
        print(
            f"{hero.name} атакує {enemy.name}. "
            f"Здоров'я ворога: {max(0, enemy.health)}"
        )


        if enemy.health <= 0:
            print(f"{enemy.name} переможений!")
            break


        hero.health -= enemy.attack
        print(
            f"{enemy.name} атакує героя. "
            f"Здоров'я героя: {max(0, hero.health)}"
        )


    if hero.health <= 0:
        print("\nГЕРОЙ ЗАГИНУВ! ПОРАЗКА!")
        break

else:
    print("\nВітаємо! Герой переміг усіх ворогів!")

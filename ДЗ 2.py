
import random

CLASSES = {
    "Warrior": {"hp": (110, 140), "attack": (10, 16)},
    "Mag": {"hp": (70, 90), "attack": (16, 24)},
}

class Hero:
    def __init__(self, name, hero_class):
        stats = CLASSES[hero_class]
        self.name = name
        self.hero_class = hero_class
        self.health = random.randint(*stats["hp"])
        self.damage = random.randint(*stats["attack"])

    def show(self):
        print(f"Ім'я: {self.name}")
        print(f"Клас: {self.hero_class}")
        print(f"Здоров'я: {self.health}")
        print(f"Шкода: {self.damage}")
        print("-" * 25)

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show(self):
        print(f"Ім'я ворога: {self.name}")
        print(f"Здоров'я: {self.health}")
        print(f"Шкода: {self.damage}")
        print("-" * 25)


goblin = Enemy("Гоблін", 50, 8)
skeleton = Enemy("Скелет", 70, 12)
dragon = Enemy("Дракон", 200, 30)

from heroes import Hero
from enemies import Enemy, goblin, skeleton, dragon

hero1 = Hero("Spider-Man", "Warrior")
hero2 = Hero("Iron Man", "Mag")

heroes = [hero1, hero2]
enemies = [goblin, skeleton, dragon]

print("=== НАШІ ГЕРОЇ ===")

for hero in heroes:
    hero.show()

print("=== ВОРОГИ ===")

for enemy in enemies:
    enemy.show()

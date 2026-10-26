
import random

CLASSES = {
    "Warrior": {"hp": (110, 140), "attack": (10, 16)},
    "Mag": {"hp": (70, 90), "attack": (16, 24)},
}

NAMES = [
    "Spider-Man",
    "Iron Man",
    "Thor",
    "Hulk",
    "Batman",
    "Superman",
    "Flash",
    "Deadpool",
    "Wolverine",
    "Captain America"
]

def create_hero(name, hero_class):
    stats = CLASSES[hero_class]
    return {
        "name": name,
        "class": hero_class,
        "hp": random.randint(*stats["hp"]),
        "attack": random.randint(*stats["attack"]),
    }

def power(hero):
    return hero["hp"] // 10 + hero["attack"] * 2

def best_hero(party):
    strongest = party[0]

    for hero in party:
        if power(hero) > power(strongest):
            strongest = hero

    return strongest

def show_hero(hero):
    print(f"Ім'я: {hero['name']}")
    print(f"Клас: {hero['class']}")
    print(f"HP: {hero['hp']}")
    print(f"Атака: {hero['attack']}")
    print(f"Сила: {power(hero)}")
    print("-" * 25)

party = []

names = random.sample(NAMES, 5)

for name in names:
    hero_class = random.choice(list(CLASSES.keys()))
    party.append(create_hero(name, hero_class))

print("=== ЗАГІН СУПЕРГЕРОЇВ ===")

for hero in party:
    show_hero(hero)

strongest = best_hero(party)

print("\n=== НАЙСИЛЬНІШИЙ СУПЕРГЕРОЙ ===")
show_hero(strongest)

print(f"Переможець: {strongest['name']}")
print(f"Його сила: {power(strongest)}")

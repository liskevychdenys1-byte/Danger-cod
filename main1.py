
from Items import Item, Weapon, Potion, Inventory



class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack



hero = Hero("Ден", 100, 20)


sword = Weapon("Залізний меч", 15, "рідкісний")
potion = Potion("Зілля здоров'я", 30, "звичайний")


inventory = Inventory()


inventory.add(sword)
inventory.add(potion)


print("=== ІНВЕНТАР ГЕРОЯ ===")

for item in inventory.items:
    print(item)

print(f"\nКількість предметів: {len(inventory)}")


print("\n=== ХАРАКТЕРИСТИКИ ГЕРОЯ ===")
print(f"Атака: {hero.attack}")
print(f"HP: {hero.health}")


print("\n=== ЕКІПІРУВАННЯ ЗБРОЇ ===")
sword.equip(hero)

print(f"Нова атака героя: {hero.attack}")

print("\n=== ВИКОРИСТАННЯ ЗІЛЛЯ ===")
hero.health -= 50
potion.use(hero)

print(f"Здоров'я героя: {hero.health}")

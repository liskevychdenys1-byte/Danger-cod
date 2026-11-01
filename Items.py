class Item:
    def __init__(self, name, power, rarity="звичайний"):
        self.name = name
        self.power = power
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} | Рідкість: {self.rarity} | Сила: {self.power}"


class Weapon(Item):
    def equip(self, hero):
        hero.attack += self.power
        print(f"{hero.name} екіпірував {self.name}!")


class Potion(Item):
    def use(self, hero):
        hero.health += self.power
        print(f"{hero.name} використав {self.name}!")
        print(f"Відновлено {self.power} HP")


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

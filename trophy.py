
def show_dungeon_results(inventory):
    print("\n========== ПІДСУМКИ ПІДЗЕМЕЛЛЯ ==========")


    best_items = sorted(
        inventory,
        key=lambda item: item["power"],
        reverse=True
    )[:3]

    print("\n ТОП-3 НАЙСИЛЬНІШІ ПРЕДМЕТИ:")
    for item in best_items:
        print(f'{item["name"]} — сила: {item["power"]}')


    rare_items = [
        item for item in inventory
        if item["rarity"] in ["Rare", "Epic"]
    ]

    print("\n💎 РІДКІСНІ ТА ЕПІЧНІ ПРЕДМЕТИ:")
    for item in rare_items:
        print(f'{item["name"]} — {item["rarity"]}')


    total_power = sum(
        item["power"] for item in inventory
    )

    print(f"\n️ ЗАГАЛЬНА СИЛА ІНВЕНТАРЯ: {total_power}")
    print("=========================================")



inventory = [
    {"name": "Залізний меч", "power": 25, "rarity": "Common"},
    {"name": "Чарівний посох", "power": 80, "rarity": "Epic"},
    {"name": "Сталевий щит", "power": 40, "rarity": "Rare"},
    {"name": "Золотий лук", "power": 65, "rarity": "Epic"},
    {"name": "Шкіряна броня", "power": 15, "rarity": "Common"},
]

show_dungeon_results(inventory)

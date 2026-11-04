
# Інвентар гравця після проходження підземелля
inventory = [
    {"name": "Залізний меч", "power": 25, "rarity": "Звичайний"},
    {"name": "Щит дракона", "power": 80, "rarity": "Епічний"},
    {"name": "Чарівний посох", "power": 65, "rarity": "Рідкісний"},
    {"name": "Старий лук", "power": 30, "rarity": "Звичайний"},
    {"name": "Меч короля", "power": 100, "rarity": "Епічний"},
    {"name": "Кинджал тіней", "power": 55, "rarity": "Рідкісний"},
    {"name": "Амулет сили", "power": 45, "rarity": "Звичайний"}
]


def dungeon_results(inventory):
    print("\n========== ПІДСУМКИ ГРИ ==========")

    # 1. Три найсильніші предмети (sorted + lambda)
    strongest_items = sorted(
        inventory,
        key=lambda item: item["power"],
        reverse=True
    )[:3]

    print("\nТри найсильніші предмети:")
    for item in strongest_items:
        print(f'{item["name"]} — сила: {item["power"]}')

    # 2. Рідкісні та епічні предмети (comprehension)
    rare_items = [
        item for item in inventory
        if item["rarity"] in ["Рідкісний", "Епічний"]
    ]

    print("\nРідкісні та епічні предмети:")
    for item in rare_items:
        print(
            f'{item["name"]} — '
            f'{item["rarity"]}, сила: {item["power"]}'
        )

    # 3. Загальна сила всіх предметів (sum + comprehension)
    total_power = sum(
        [item["power"] for item in inventory]
    )

    print(f"\nЗагальна сила інвентаря: {total_power}")
    print("=================================")


# Завершення підземелля
print("Вітаємо! Ви пройшли підземелля!")
dungeon_results(inventory)

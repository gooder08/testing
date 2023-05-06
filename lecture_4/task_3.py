def max_value():
    stats = {
        "facebook": 55,
        "yandex": 120,
        "vk": 115,
        "google": 99,
        "email": 42,
        "ok": 98,
    }
    max_value = max(stats.values())
    for k, v in stats.items():
        if v == max_value:
            return f"Канал с максимальным обьемом продаж: {k}"

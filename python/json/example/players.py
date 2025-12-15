import json

# 1. Зчитуємо JSON з файлу
with open("players.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 2. Обчислюємо середню кількість очок для кожного гравця
for player in data["players"]:
    points = player["points"]
    average_points = sum(points) / len(points)
    player["average_points"] = average_points

# 3. Записуємо оновлені дані у новий JSON-файл
with open("players_with_average.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Файл players_with_average.json створено!")

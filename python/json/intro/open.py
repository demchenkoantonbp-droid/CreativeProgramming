import json

# Відкриваємо файл і зчитуємо JSON
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Перевіряємо, що зчиталося
print(data)
print(type(data))

print(data["name"])
print(data["age"])
print(data["subjects"][1])  # Інформатика


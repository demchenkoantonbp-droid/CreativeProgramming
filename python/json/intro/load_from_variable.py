import json

json_text = '''
{
  "city": "Lviv",
  "temperature": [12, 14, 16]
}
'''

data = json.loads(json_text)
print(data["city"])

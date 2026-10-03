number = int(input('Скільки піц замовляєте? '))
cost = float(input('Скільки коштує одна піца? '))

total = number * cost
print('Ціна без знижки', total)

# Скидка 10% применяется только к каждой четной пицце
even_pizzas = number // 2
discount = even_pizzas * cost * 0.1

print('Знижка', discount)
total = total - discount
print('Ціна зі знижкою', total)

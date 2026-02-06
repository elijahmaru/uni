# Упаковка в кортеж (tuple packing)
packed_tuple = 1, 2, 3, 4
print("Упакованный кортеж:", packed_tuple)

# Распаковка кортежа (tuple unpacking)
a, b, c, d = packed_tuple
print(f"Распаковка: a={a}, b={b}, c={c}, d={d}")

# Распаковка с использованием *
first, *middle, last = packed_tuple
print(f"Распаковка с *: first={first}, middle={middle}, last={last}")

# Использование распаковки при обмене значений
x, y = 10, 20
print(f"До обмена: x={x}, y={y}")
x, y = y, x  # Обмен значениями с помощью распаковки
print(f"После обмена: x={x}, y={y}")
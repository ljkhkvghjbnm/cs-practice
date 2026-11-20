a = float(input('введите стоимость тетради '))
b = float(input('введите количество тетрадей '))
res = round(a*b, 2)
print(f'стоимость: {res.evalf(2)}')
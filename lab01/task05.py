b = int(input('введите количество секунд '))
h = b//3600
min = (b%3600)//60
sek = (b%3600)%60
print(f'{h} часов')
print(f'{min} минут')
print(f'{sek} секунд')
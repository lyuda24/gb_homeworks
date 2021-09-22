percent = int(input('Введите число процента от 1 до 100: '))

if 11 <= percent <= 14:
    word = 'процентов'
elif percent % 10 == 1:
    word = 'процент'
elif 2 <= percent % 10 <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(word)
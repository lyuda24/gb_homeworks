duration = int(input('Введите время в секундах: '))

days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)
min = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
sec = (duration - days * (60 * 60 * 24) - hours * (60 * 60) - min * 60)
print(days, 'дн', hours, 'час', min, 'мин', sec, 'сек')



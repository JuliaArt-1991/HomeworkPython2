# Задача 20

eng = {1: 'AEIOULNSTR',
       2: 'DG',
       3: 'BCMP',
       4: 'FHVWY',
       5: 'K',
       8: 'JZ',
       10: 'QZ'}
rus = {1: 'АВЕИНОРСТ',
       2: 'ДКЛМПУ',
       3: 'БГЁЬЯ',
       4: 'ЙЫ',
       5: 'ЖЗХЦЧ',
       8: 'ШЭЮ',
       10: 'ФЩЪ'}
n = abs(int(input('Выберите раскладку: 1 - английская раскладка, 0 - русская раскладка: ')))
word = input('Введите слово: ').upper()
if n == 1:
    summ = 0
    for i in word:
        for k, v in eng.items():
            if i in v:
                summ += k
    print(f"Стоимость слова: {summ}")
else:
    summ = 0
    for i in word:
        for k, v in rus.items():
            if i in v:
                summ += k
    print(f"Стоимость слова: {summ}")

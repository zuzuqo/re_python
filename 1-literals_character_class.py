import re

text = 'Карта map и объект bitmap - это разные вещи'

# выделяет map в text, причем map является целым словом
match = re.findall(r'\bmap\b', text)
print(match)

text = '--Еда, беду, 553 4901 -1 2 победа'
# выделяет слова, в которых как большая, так и маленькая букву "е" в начале, а также как "а", так "у" в конце
match = re.findall(r'[еЕ]д[ау]', text)
print(match)

# выделяет цифры в строке
match = re.findall(r'[0-9]', text)
print(match)

# выделяет 2 любые цифры, идущие подряд
match = re.findall(r'[0-9][0-9]', text)
print(match)

# тут еще дефис может быть выделен
match = re.findall(r'[-0-9][-0-9]', text)
print(match)

# инверсия предыдущего примера (выделяются не цифры и не дефис по два)
match = re.findall(r'[^-0-9][^-0-9]', text)
print(match)

# выделяются все буквы из русского алфавита
match = re.findall(r'[а-яА-ЯёЁ]', text)
print(match)

# более короткие записи

# любой символ кроме переноса строки
match = re.findall(r'.', text)
print(f'.: {match}')

# любая цифра
match = re.findall(r'[\d]', text)
print(f'[\d]: {match}')

# любая не цифра
match = re.findall(r'[\D]', text)
print(f'[\D]: {match}')

# любой пробельный символ (в том числе табуляции, переноса строки...)
match = re.findall(r'[\s]', text)
print(f'[\s]: {match}')

# любой не пробельный символ
match = re.findall(r'[\S]', text)
print(f'[\S]: {match}')

# любой символ слова
match = re.findall(r'[\w]', text)
print(f'[\w]: {match}')

# любой символ слова но только латинские буквы
match = re.findall(r'[\w]', text, re.ASCII)
print(f'[\w] ASCII: {match}')

# любой не символ слова
match = re.findall(r'[\W]', text)
print(f'[\W]: {match}')

# выделение чисел в шестнадцатиричном формате
text = "0xf, 0xa, это никогда не попадет в match, 0x5, 19"
match = re.findall(r'0x[\da-fA-F]', text)
print(match)

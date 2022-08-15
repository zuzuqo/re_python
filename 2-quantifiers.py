import re

text = 'Google, Goooogle, Goooooooooogle'
print(text)

# жадный (мажорный) квантификатор o{2,5} который ищет последовательность "о" от 2 до 5 символов, выбирая последовательность максимальной длины
match = re.findall(r'o{2,5}', text)
print(f'o major 2-5: {match}')

# минорый квантификатор o{2,5}? который ищет последовательность "о" от 2 до 5 символов, выбирая последовательность минимальной длины
match = re.findall(r'o{2,5}?', text)
print(f'o minor 2-5: {match}')

# выделяет, если есть 4 "o" между "G" и "gle"
match = re.findall(r'Go{4}gle', text)
print(f'o 5: {match}')

# выделяет, если есть 2+ "o" между "G" и "gle"
match = re.findall(r'Go{2,}gle', text)
print(f'o major 2-: {match}')

# выделяет, если есть <5 "o" между "G" и "gle"
match = re.findall(r'Go{,5}gle', text)
print(f'o major -5: {match}')

# выделяет, если есть 2+ "o" между "G" и "gle"
match = re.findall(r'Go{2,}?gle', text)
print(f'o minor 2-: {match}')

# выделяет, если есть <5 "o" между "G" и "gle"
match = re.findall(r'Go{,5}?gle', text)
print(f'o minor -5: {match}')

phone = '89123456780, 7930123423, mail@gmail.com, 11123459530, 89876543210'
match = re.findall(r'8\d{10}', phone)
print(f'correct phone number: {match}')

text = 'стеклянный, стекляный'

# аналог {0,1}
match = re.findall(r'стеклянн?ый', text)
print(match)

# аналог {1,}
match = re.findall(r'стеклян+ый', text)
print(match)

# аналог {0,}
match = re.findall(r'стеклян*ый', text)
print(match)

# тут парсится строка
text = 'author=Пушкин А.С.; title=Евгений Онегин; price=200; year=2001'
match = re.findall(r'(\w+)\s*=\s*([^;]+)', text)
print(match)

# при парсинге html документов обычно используется минорный квантификатор, поскольку жадный может начать работать не с тем окончанием тега
text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'
match = re.findall(r'<img.*?>', text)                   # минорный взял наиболее короткую последовательность
print(match)
match = re.findall(r'<img.*>', text)                    # мажорный взял лишнее
print(match)
match = re.findall(r'<img[^>]*>', text)                 # альтернатива
print(match)

match = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]+>', text)                 # более правильный вариант с проверкой на наличие атрибута src у тега img
print(match)

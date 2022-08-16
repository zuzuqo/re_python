import re

text = '<font color=#CC0000>'

match = re.search(r'(\w+)=(#[\da-fA-F]{6})\b', text)
print(f"match: {match}")

print(f"match.group():\t\t{match.group()}")
print(f"match.group(0):\t\t{match.group(0)}")
print(f"match.group(1):\t\t{match.group(1)}")
print(f"match.group(2):\t\t{match.group(2)}")

# число групп
print(f"match.lastindex:\t{match.lastindex}")

# начальная позиция в тексте у определенной группы, иначе -1
print(f"match.start(1):\t\t{match.start(1)}")        # 1 группа
print(f"match.start(2):\t\t{match.start(2)}")        # 2 группа

# конечная позиция в тексте у определенной группы, иначе -1
print(f"match.end(1):\t\t{match.end(1)}")        # 1 группа
print(f"match.end(2):\t\t{match.end(2)}")        # 2 группа

# кортеж с начальной и конечно позицией
print(f"match.span(1):\t\t{match.span(1)}")        # 1 группа
print(f"match.span(2):\t\t{match.span(2)}")        # 2 группа

# первый индекс, в котором осуществлялась проверка
print(f"match.pos:\t\t\t{match.pos}")
# последний индекс, в котором осуществлялась проверка
print(f"match.endpos:\t\t{match.endpos}")

# возвращает анализируемую строку
print(f"match.string:\t\t{match.string}")

# возвращает скомпилированный шаблон
print(f"match.re:\t\t\t{match.re}")

match = re.search(r'(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b', text)
# словарь
print(f"match.groupdict():\t{match.groupdict()}")

# возвращает имя последней группы или None, если их нет
print(f"match.lastgroup:\t{match.lastgroup}")

# преобразовывает в определенный формат. более предпочтительно
m = match.expand(r'\g<key>:\g<value>')
print(f"match.expand(args):\t{m}")

# аналогично, но используются индексы групп. отриательно скажется при поддержке проекта
m = match.expand(r'\1:\2')
print(f"match.expand(args):\t{m}")

text = "<font color=#CC0000 bg=#ffffff>"

# search видит только первое вхождение. остальное игнорирует
match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(f'match: {match}')

# match теперь итерируемый объект
match = re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(f'match: {match}')
print(f"next(match):\t\t{next(match)}")
print(f"next(match):\t\t{next(match)}")
# print(f"next(match):\t\t{next(match)}")   # ошибка StopIteration

match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(f"match:\t\t{match}")

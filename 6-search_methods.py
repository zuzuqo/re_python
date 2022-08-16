import re

text = '+7(123)456-78-90'

# ищет совпадения с самого начала
match = re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', text)
print(match)

text = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""

# разделение текста по символам \n ; ,
ar = re.split(r'[\n;,]+', text)
print(ar)

text = """Москва
Казань
Тверь
Самара
Уфа"""

# text в следующий формат
# <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>

# преобразование в определенный формат
l = re.sub(r'\s*(\w+)\s*', r'<option>\1<option>\n', text)
print(l)

count = 0
def replFind(m):
    global count
    count += 1
    return f'<option value="{count}">{m.group(1)}</option>\n'

# преобразование с использованием функции
l = re.sub(r'\s*(\w+)\s*', replFind, text)
print(l)

# возвращает преобразованную строку и число замен
l, total = re.subn(r'\s*(\w+)\s*', r'<option>\1<option>\n', text)
print(l, total)

# заранее компилируется шаблон
rx = re.compile(r'\s*(\w+)\s*')
# после шаблон используется
l1, total = rx.subn(r'<option>\1<option>\n', text)
l2 = rx.sub(replFind, text)
print(l1, total)
print(l2)

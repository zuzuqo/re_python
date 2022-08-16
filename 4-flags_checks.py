import re

text = 'подоходный налог, доход'

# поиск следующих слов c помощью \b границы слова
match = re.findall(r"\b(прибыль|обретение|доход)\b", text)
print(match)

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

# содержимое тега script
match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)

# ретроспективная проверка (опережающая)
match = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text, re.MULTILINE)
print(match)

# поиск ключей значений (с ретроспективной проверкой из-за которой игнорируются случайные пробелы в атрибутах)
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"\']([^\"\']+)(?<![ \t])", text, re.MULTILINE)
print(match)

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type " content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""

# вывод всех ключей значений самых разных видов
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE)
print(match)

# использование флагов и комментариев
match = re.findall(r"""([-\w]+)             #выделяем атрибут
                   [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
                   (?P<q>[\"'])?            #проверяем наличие кавычки
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
                   """,
                   text, re.MULTILINE|re.VERBOSE)
print(match)

text = 'Python, python, PYTHON'

match = re.findall(r"python", text)
print(match)

# использование флагов внутри регулярных выражений (тут используется флаг I (IGNORECASE
match = re.findall(r"(?im)python", text)
print(match)

# аналогично, но без флага внутри выражения
match = re.findall(r"python", text, re.I)
print(match)
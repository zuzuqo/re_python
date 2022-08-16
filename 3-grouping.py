import re

text = 'lat = 5, lon=72, par=9049, asd=24'

match = re.findall(r'\w+\s*=\s*\d+', text)
print(match)

# выделение lat и/или lon
match = re.findall(r'(?:lat|lon)\s*=\s*\d+', text)
print(match)

# выделение lat и/или lon без значений
match = re.findall(r'(lat|lon)\s*=\s*\d+', text)
print(match)

# выделение lat и/или lon
match = re.findall(r'((lat|lon)\s*=\s*\d+)', text)
print(match)

# выделение ключа и значения lat и/или lon
match = re.findall(r'(lat|lon)\s*=\s*(\d+)', text)
print(match)

text = '<p>Картинка <img src="bg.jpg"> в тексте</p>'

match = re.findall(r'<img\s+[^>]*src=[\'"](.+?)[\'"]', text)
print(match)

# обращение по имени q
match = re.findall(r'(<img)\s+[^>]*src=(?P<q>[\'"])(.+?)(?P=q)', text)
print(match)

# работа с map.xml

# не лучшее решение, поскольку лучше использовать имена сохраняющих групп для обращения
with open('map.xml', 'r') as f:
    lat = []
    lon = []
    for text in f:
        match = re.findall(r"<point\s+[^>]*?lon=([\"\'])([\d.,]+)\1\s+[^>]*lat=([\"\'])([\d.,]+)\1", text)
        if match != []:
            lat.append(match[0][1])
            lon.append(match[0][3])

print(lat)
print(lon)

with open('map.xml', 'r') as f:
    lat = []
    lon = []
    d = []
    for text in f:
        match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[\d.,]+)\1\s+[^>]*lat=([\"\'])(?P<lat>[\d.,]+)\1", text)
        if match:
            v = match.groupdict()
            d.append(v)
            if 'lon' in v and 'lat' in v:
                lat.append(v['lat'])
                lon.append(v['lon'])

print(lat)
print(lon)
print(d)

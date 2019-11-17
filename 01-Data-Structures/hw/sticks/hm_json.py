with open('winedata_1.json', 'r') as f:
    winedata_1 = f.read()

with open('winedata_2.json', 'r') as f:
    winedata_2 = f.read()


def parser(json):
    data = []
    json = str(json)
    json = json.replace('[{"', '')
    json = json.replace('}]', '')
    json = json.replace('null', '0')
    for string in json.split('}, {"'):
        keys, values = [], []
        for key_value in string.split(', "'):
            keys.append(key_value.split('": ')[0])
            values.append(key_value.split('": ')[1])
            for i in range(len(values)):
                values[i] = values[i].replace('"', '')
        data.append(dict(zip(tuple(keys), tuple(values))))
    return data


def merge(file1, file2):
    full = file1
    for i in file2:
        if i not in full:
            full.append(i)
    return full


def sort_inf(inf):
    sort = sorted(inf, key=lambda k: int(k['price']), reverse=True)
    return sort


winedata_1 = parser(winedata_1)
winedata_2 = parser(winedata_2)
winedata_full = merge(winedata_1, winedata_2)
sorted_full_data = sort_inf(winedata_full)


with open('winedata_full.json', 'tw', encoding='utf-8') as out:
    out.write('[')
    for line in winedata_full:
        out.write(f'{line},\n')
    size = out.tell()
    out.truncate(size - 2)
    out.write(']')


varietes = ['Gew\\u00fcrztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend']
info = ['avarege_price', 'min_price', 'max_price', 'most_common_region', 'most_common_country', 'avarage_score']
for_statistics = {}
for item in varietes:
    for_statistics[item] = {}
    for key in info:
        for_statistics[item][key] = 0


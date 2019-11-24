from collections import Counter
import numpy as np
import statistics


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
    full = file2.copy()
    for i in file1:
        if i not in file2:
            full.append(i)
    return full


def sort_inf(info):
    sort = sorted(info, key=lambda k: (-int(k['price']), k['variety']))
    return sort


winedata_1 = parser(winedata_1)
winedata_2 = parser(winedata_2)
winedata_full = merge(winedata_1, winedata_2)
sorted_full_data = sort_inf(winedata_full)


# запись в файл winedata_full.json
with open('winedata_full.json', 'tw', encoding='utf-8') as out:
    out.write('[')
    for line in winedata_full:
        out.write(f'{line},\n')
    size = out.tell()
    out.truncate(size - 2)
    out.write(']')


varieties = ['Gew\\u00fcrztraminer', 'Riesling', 'Merlot', 'Madera',
            'Tempranillo', 'Red Blend']
info = ['average_price', 'min_price', 'max_price', 'most_common_region',
        'most_common_country', 'average_score']
for_statistics = {}
for item in varieties:
    for_statistics[item] = {}
    for key in info:
        for_statistics[item][key] = None


def stats(variety, stat,  winedata):
    prices = []
    most_com_region = []
    most_com_country = []
    average_score = []
    for wine in winedata:
        if wine['variety'] == variety:
            if wine['price'] != '0':
                prices.append(int(wine['price']))
            if wine['province'] != '0':
                most_com_region.append(wine['province'])
            if wine['country'] != '0':
                most_com_country.append(wine['country'])
            if wine['points'] != '0':
                average_score.append(int(wine['points']))
    try:
        stat['average_price'] = statistics.mean(prices)
        stat['max_price'] = max(prices)
        stat['min_price'] = min(prices)
        stat['most_common_region'] = Counter(most_com_region).most_common()[0][0]
        stat['most_common_country'] = Counter(most_com_country).most_common()[0][0]
        stat['average_score'] = statistics.mean(average_score)
    except statistics.StatisticsError:
        None

    return stat


# статистика по сортам
for wine in for_statistics:
    stats(wine, for_statistics[wine], winedata_full)

common_stats = for_statistics


# наиболее дешевые и дорогие вина
names = []
prices = []

for wine in winedata_full:
    if wine['price'] != '0':
        prices.append(int(wine['price']))
        names.append(wine['title'])

prices = np.array(prices)
max_index = np.where(prices == max(prices))[0]
min_index = np.where(prices == min(prices))[0]


most_expensive_wine = {f"{names[i]}'": prices[i] for i in max_index}
cheapest_wine = {f"{names[i]}'": prices[i] for i in min_index}


# вина с высшей и низшей оценкой
names = []
scores = []

for wine in winedata_full:
    if wine['points'] != '0':
        scores.append(int(wine['points']))
        names.append(wine['title'])

scores = np.array(scores)
max_index = np.where(scores == max(scores))[0]
min_index = np.where(scores == min(scores))[0]

highest_score = {f"{names[i]}'": scores[i] for i in max_index}
lowest_score = {f"{names[i]}'": scores[i] for i in min_index}


# в среднем самое дорогое и дешевое вино среди стран
countries = []
means = []

for wine in winedata_full:
    if wine['country'] != '0' and wine['price'] != '0':
        if wine['country'] not in countries:
            countries.append(wine['country'])

for country in countries:
    prices = []
    for wine in winedata_full:
        if wine['country'] == country and wine['price'] != '0':
            prices.append(int(wine['price']))
    means.append(statistics.mean(prices))

means = np.array(means)
max_index = np.where(means == max(means))[0]
min_index = np.where(means == min(means))[0]

most_expensive_country = {f"{countries[i]}'": means[i] for i in max_index}
cheapest_country = {f"{countries[i]}'": means[i] for i in min_index}


# most_rated_country & underrated_country
countries = []
points = []
means = []

for wine in winedata_full:
    if wine['country'] != '0' and wine['points'] != '0':
        if wine['country'] not in countries:
            countries.append(wine['country'])

for country in countries:
    points = []
    for wine in winedata_full:
        if wine['country'] == country and wine['points'] != '0':
            points.append(int(wine['points']))
    means.append(statistics.mean(points))

means = np.array(means)
max_index = np.where(means == max(means))[0]
min_index = np.where(means == min(means))[0]

most_rated_country = {f"{countries[i]}'": means[i] for i in max_index}
underrated_country = {f"{countries[i]}'": means[i] for i in min_index}


# most_active_commentator
taster_names = []

for wine in winedata_full:
    if wine['taster_name'] != '0':
        taster_names.append(wine['taster_name'])

most_active_commentator = Counter(taster_names).most_common()[0][0]


# запись в файл stats.json
with open('stats.json', 'w') as f:
    f.write('{"statistics": ')
    f.write('{"wine": ')
    f.write(str(for_statistics).replace('\'', '"'))
    f.write(f',"most_expensive_wine": {most_expensive_wine}, ')
    f.write(f'"cheapest_wine": {cheapest_wine}, ')
    f.write(f'"highest_score": {highest_score}, ')
    f.write(f'"lowest_score": {lowest_score}, ')
    f.write(f'"most_expensive_country": {most_expensive_country}, ')
    f.write(f'"cheapest_country": {cheapest_country}, ')
    f.write(f'"most_rated_country": {most_rated_country}, ')
    f.write(f'"underrated_country": {underrated_country}, ')
    f.write(f'"most_active_commentator": "{most_active_commentator}"')
    f.write('}}')


def markdown(item):

    replaces = (('{', '\n\n\n'), (',', '\n'), ('}', '\n\n\n'), ('"', '\t'),
                ("'", ''))
    for replace in replaces:
        item = str(item).replace(*replace)

    return item


with open('stats.md', 'w') as f:
    f.write(markdown(f'# Statistics: #\n## Wine:\n{common_stats}\n'))
    f.write(markdown('## Most expensive wine: ##'))
    f.write(markdown(most_expensive_wine))
    f.write(markdown('## Cheapest wine: ##'))
    f.write(markdown(cheapest_wine))
    f.write(markdown('## Highest score: ##'))
    f.write(markdown(highest_score))
    f.write(markdown('## Lowest score: ##'))
    f.write(markdown(lowest_score))
    f.write(markdown('## Most expensive country: ##'))
    f.write(markdown(most_expensive_country))
    f.write(markdown('## Cheapest country: ##'))
    f.write(markdown(cheapest_country))
    f.write(markdown('## Most rated country: ##'))
    f.write(markdown(most_rated_country))
    f.write(markdown('## Underrated country: ##'))
    f.write(markdown(underrated_country))
    f.write(markdown('## Most active commentator: '))
    f.write(markdown(most_active_commentator))


"""
File .env contains two variables:
USERNAME = example_user_name
PWD = example_password
for authentication on pikabu.ru
"""

import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PWD')
url = 'https://pikabu.ru'
auth = {'username': username, 'password': password}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}


# parsing
def parse(url):
    rows_all = []
    for page in range(1, 6):
        resp = requests.get(f'http://pikabu.ru/?page={page}', headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        rows = soup.find_all('a', {'class': 'tags__tag', 'data-tag-menu': True})
        rows_all.append(rows)
    return rows_all


# counting tags
def tags_count(data):
    tags = {}
    tagscount = 0
    for resultset in data:
        for row in resultset:
            tag = row.get_text()
            tagscount += 1
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] += 1
    return tagscount, tags


# tagging top
def top(data):
    sorted_tags = sorted(data.items(), key=lambda t: t[1])[-10:]
    return sorted_tags


if __name__ == '__main__':
    session = requests.Session()
    post = session.post(url, data=auth, headers=headers)
    print(f'Status code: {post.status_code}')
    parsed_data = parse(url)
    counted_tags = tags_count(parsed_data)[0]
    tags = tags_count(parsed_data)[1]
    top10 = top(tags)

    # outputting results
    print('------------\nTop 10 tags\n------------')
    for tag in reversed(top10):
        print(f'{tag[0]}: {tag[1]}')
    print(
        f'------------\nCounted tags: {counted_tags}\n------------')

    # writing results to txt file
    with open('top10_tags_pikabu.txt', 'w', encoding='utf8') as file:
        file.write('------------\nTop 10 tags\n------------\n')
        for tag in reversed(top10):
            file.write(f'{tag[0]}: {tag[1]}\n')
        file.write(f'------------\nCounted tags: {counted_tags}\n------------')

import requests
import os

from pprint import pprint

# задание 1
url = "https://superheroapi.com/api/2619421814940190/"
list_hero = dict()
hero_name = ['Hulk', 'Captain America', 'Thanos']

# получаем id и параметр intelligence
for nm in hero_name:
    a = url+'search/'+nm+'/'
    b = requests.get(a).json()

    for element in b.get('results')[:]:
        if element.get('name') == nm:
            f = element.get('id')
            d = requests.get(url+f+'/powerstats').json()
            list_hero[nm] = int(d.get('intelligence'))

# print(list_hero)

# получаем имя героя с максимальным intelligence
max_volume=list(set(list_hero.values()))
max_num= 0
for i in max_volume:
  if i > max_num:
    max_num=i

inv_stats = {value: key for key, value in list_hero.items()}
print()
pprint('Max intelligence - ' + inv_stats[max_num])


# задание 2
file_link = input('Введине путь к файлу: ')
a = os.path.abspath(file_link)
tk = input('Введите токен: ')


class YaUploader:
    def __init__(self, token: str):
        self.token = tk

    def upload(self, file_path: str):
        name_file = os.path.basename(file_link)
        """Метод загруджает файл file_path на яндекс диск"""
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': name_file},
                                headers={'Authorization': f'OAuth {tk}'})
        # print(response.status_code)
        # pprint(response.json())
        href = response.json()['href']
        with open(name_file) as f:
            requests.put(href, files={'file': f})
        return print('Файл загружен')


if __name__ == '__main__':
    uploader = YaUploader(tk)
    result = uploader.upload(a)
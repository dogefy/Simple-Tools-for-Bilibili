import requests
import bs4
import re

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
}


def get_uid(name):
    id = []
    url = 'https://search.bilibili.com/upuser?keyword={}'.format(name)
    get_page = requests.get(url)
    soup = bs4.BeautifulSoup(get_page.content, 'lxml')
    uid_pattern = re.compile('space.bilibili.com/([0-9]+)')
    uid_match = uid_pattern.findall(str(soup.select('.title')))
    if len(uid_match) == 0:
        id.append(-1)
        return id
    else:
        name_pattern = re.compile('target="_blank" title="(.+?)"')
        name_match = name_pattern.findall(str(soup.select('.title')))
        id.append(uid_match[0])
        id.append(name_match[0])
        return id


if __name__ == '__main__':
    name = input('Please input the name : ')
    uid = get_uid(name)
    if uid[0] == -1:
        print("Can not find the user with similar name to '{}'.".format(name))
    else:
        print('The UID of {} : {}'.format(uid[1], uid[0]))

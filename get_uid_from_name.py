import requests
import bs4
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}


def get_uid(name):
    url = 'https://search.bilibili.com/upuser?keyword={}'.format(name)
    a = requests.get(url)
    soup = bs4.BeautifulSoup(a.content, 'lxml')
    match = re.search(r'space.bilibili.com/([0-9]+)', str(soup.select('.title')))
    try:
        match.group(0)
    except AttributeError:
        return -1
    else:
        match = re.search(r'[0-9]+', str(match.group(0)))
        return match.group(0)


if __name__ == '__main__':
    name = input('Please input the name : ')
    uid = get_uid(name)
    if uid == -1:
        print('Can not find the user with similar name to {}.'.format(name))
    else:
        print('The UID of {} :'.format(name), uid)

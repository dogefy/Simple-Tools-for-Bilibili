import requests
import json
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}


def get_info(uid):
    url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(uid)
    info_page = requests.get(url, headers=headers)
    info = json.loads(info_page.content.decode())['data']
    info_sex = info['sex']
    info_name = info['name']
    info_sign = info['sign']
    info_birthday = info['birthday']
    info_mid = info['mid']
    info_face = info['face']
    if info_birthday == '':
        info_birthday = 'unknown'
    info_sign = re.sub(r'\n', ' ', info_sign)
    print('姓名：{} UID：{}'.format(info_name, info_mid))
    print('性别：{} 生日：{}'.format(info_sex, info_birthday))
    print('签名：{}'.format(str(info_sign)))


def get_stats(uid):
    url = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp'.format(uid)
    stats_page = requests.get(url, headers=headers)
    stats = json.loads(stats_page.content.decode())['data']
    stats_fans = stats['follower']
    stats_followings = stats['following']
    print('粉丝数：{} 关注人数：{}'.format(stats_fans, stats_followings))


if __name__ == '__main__':
    uid = input('Please input UID : ')
    uid = int(uid)
    get_info(uid)
    get_stats(uid)

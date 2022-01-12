import requests
import json
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}

f = open("f.txt", 'w')
face = open('face.jpg', 'wb')


def get_info(uid):
    info = {}
    url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(uid)
    info_page = requests.get(url, headers=headers)
    info_json = json.loads(info_page.content.decode())['data']
    info['sex'] = info_json['sex']
    info['name'] = info_json['name']
    info['sign'] = info_json['sign']
    info['birthday'] = info_json['birthday']
    info['uid'] = info_json['mid']
    info['face'] = info_json['face']
    if info['birthday'] == '':
        info['birthday'] = 'unknown'
    info['sign'] = re.sub(r'\n', ' ', info['sign'])
    get_face = requests.get(info['face'], headers=headers)
    face.write(get_face.content)
    return info


def get_stats(uid):
    stats = {}
    url = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp'.format(uid)
    stats_page = requests.get(url, headers=headers)
    stats_json = json.loads(stats_page.content.decode())['data']
    stats['fans'] = stats_json['follower']
    stats['followings'] = stats_json['following']
    return stats


if __name__ == '__main__':
    uid = input('Please input UID : ')
    uid = int(uid)
    info = get_info(uid)
    stats = get_stats(uid)
    print('姓名：{} UID：{}'.format(info['name'], info['uid']))
    print('性别：{} 生日：{}'.format(info['sex'], info['birthday']))
    print('签名：{}'.format(str(info['sign'])))
    print('粉丝数：{} 关注人数：{}'.format(stats['fans'], stats['followings']))
    f.write('name:{}\nuid:{}\nsex:{}\nbirthday:{}\nsign:{}\n'.format(info['name'], info['uid'], info['sex'],
                                                                     info['birthday'], info['sign']))
    f.write('fans:{}\nfollowings:{}'.format(stats['fans'], stats['followings']))

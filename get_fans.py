import time
import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}

uid = 208259
url_init = 'https://api.bilibili.com/x/relation/followings?vmid={}&pn=1&ps=20&order=desc&jsonp=jsonp'.format(uid)
count = 0

if __name__ == '__main__':
    a = requests.get(url_init, headers=headers)
    followings = json.loads(a.content.decode())
    total = followings['data']['total']
    urls = ['https://api.bilibili.com/x/relation/followings?vmid={}&pn={}&ps=50&order=desc&jsonp=jsonp'.format(uid, i)
            for i in range(1, total // 50 + 2)]
    for url in urls:
        a = requests.get(url, headers=headers)
        followings = json.loads(a.content.decode())
        followings_list = followings['data']['list']
        for user in followings_list:
            mid = user['mid']
            uname = user['uname']
            print(count, 'uid =', mid, 'name =', uname)
            count = count + 1
        time.sleep(5)

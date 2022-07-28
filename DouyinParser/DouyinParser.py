'''
Author: Vincent Young
Date: 2022-07-28 20:00:56
LastEditors: Vincent Young
LastEditTime: 2022-07-28 20:25:28
FilePath: /DouyinParser/DouyinParser/DouyinParser.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
import requests
import re

def parser(original_url):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url_list = re.findall(pattern, original_url) 
    url = url_list[0]

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Upgrade-Insecure-Requests': '1'
    }
    data = requests.get(headers=headers, url=url, timeout=5)
    vid = re.findall(r'\d+',data.url)[0]

    if(vid == ""):
        print('Error: Invalid URL')
        return None

    response = requests.get(
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+str(vid), 
        headers = headers
    )
    item = response.json().get("item_list")[0]
    
    mp4 = item.get("video").get("play_addr").get("url_list")[0].replace("playwm", "play")
    mp3 = item.get("music").get("play_url").get("url_list")[0]
    desc = item.get("desc")
    nickname = item.get("author").get("nickname")
    shortid = item.get("author").get("shortid")

    video_info = {
        'desc': desc,
        'mp4': mp4,
        'mp3': mp3,
        'nickname': nickname,
        'id': shortid
    }
    print(video_info)
    return video_info
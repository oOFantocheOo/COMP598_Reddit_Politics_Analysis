import argparse
import datetime
import json
import os.path as osp

import requests

script_dir = osp.dirname(__file__)
today = datetime.date.today()
date_str = str(today).replace('-', '')


def get_posts(subreddit_name, after):
    if not after:#here it returns a list of length 101 because there is a stickied post
        data = requests.get(f'http://api.reddit.com/r/{subreddit_name}/new?limit=100',
                            headers={'User-Agent': 'windows:requests (by /u/oOFantocheOo)'}).json()[
            'data']['children']
    else:

        data = requests.get(f'http://api.reddit.com/r/{subreddit_name}/new?limit=100&after={after}',
                            headers={'User-Agent': 'windows:requests (by /u/oOFantocheOo)'}).json()[
            'data']['children']
    for i, d in enumerate(data):
        data[i] = d['data']
    fullname = data[-1]['name']
    return data, fullname


def download(subreddit, path):
    lst, after = [], ''
    for i in range(10):
        cur_data, after = get_posts(subreddit, after)
        lst += cur_data
        print(len(lst))
    with open(path, 'w', encoding='utf-8') as f:
        for post in lst:
            f.write(json.dumps(post))
            f.write('\n')


def main():
    subreddit = 'conservative'
    download(subreddit, '1127_conservative.json')


if __name__ == "__main__":
    main()

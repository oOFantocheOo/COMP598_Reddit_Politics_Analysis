import json
import requests
import os.path as osp
import sys
import argparse

BASE_DIR = osp.dirname(osp.dirname(osp.abspath(__file__)))


def collect_data(subreddit_name, output_name):
    file_name = osp.join(osp.join(BASE_DIR, 'data'), output_name )
    f = open(file_name, 'a')
    after=''
    for i in range(0,10):
        if i==0:
            res = requests.get(f'http://api.reddit.com{subreddit_name}/new?limit=100', headers={
                            'User-Agent': 'mac:requests (by u/janesesz)'})
            after=res.json()['data']['after']
        else:
            res=requests.get(f'http://api.reddit.com{subreddit_name}/new?limit=100&after={after}', headers={
                            'User-Agent': 'mac:requests (by u/janesesz)'})
            after=res.json()['data']['after']
        posts_list = res.json()['data']['children']
        for i in posts_list:
            if i['data']['stickied']==False:
                i_json = json.dumps(i)
                f.write(i_json)
                f.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', help='The output file name. Should be a json file. Saving the files as <yyyy><mm><dd>_politics.json.')
    parser.add_argument('subreddit',help='Subreddit name.')
    args = parser.parse_args()
    output_file_name = args.o
    subreddit=args.subreddit
    collect_data(subreddit,output_file_name)

if __name__ == '__main__':
    main()
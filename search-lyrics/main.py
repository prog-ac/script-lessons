
import os
import sys
import time
import json
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
from googleapiclient.discovery import build


def get_arg():

    args = sys.argv
    return args

def output_lyrics(soup):

    #歌詞取得
    lyrics_bs = soup.find_all(id="flash_area")

    lyrics_tmp = lyrics_bs[0].getText()
    #split関数で文字列を全角の空白で分割してリスト化
    lyrics_list = lyrics_tmp.split("　")

    #歌詞
    for lyrics_line in lyrics_list:
        print(lyrics_line)

def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def get_search_response(keyword):

    GOOGLE_API_KEY          = "xxxxxxxxxxxx"
    CUSTOM_SEARCH_ENGINE_ID = "000000000000"
    DATA_DIR = 'data'
    make_dir(DATA_DIR)

    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 10
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            time.sleep(1)
            response.append(service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=10,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[0].get("startIndex")
        except Exception as e:
            #print(e)
            break

    # レスポンスをjson形式で保存
    save_response_dir = DATA_DIR
    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response
    jsonstr = json.dumps(out, ensure_ascii=False)
    with open(os.path.join(save_response_dir, today + "_" + keyword + '.json'), mode='w') as response_file:
        response_file.write(jsonstr)

def main():
    #引数取得
    args = get_arg()

    #引数から曲名を取得
    song_name = ""
    for i in range(1, len(args)):
        song_name = song_name + args[i]
        if (i + 1) != len(args):
            song_name = song_name + " "

    #jsonfile作成
    get_search_response(song_name)

    today = datetime.datetime.today().strftime("%Y%m%d")
    file_name = "./data/" + today + "_" + song_name + ".json"

    json_open = open(file_name, 'r')
    json_load = json.load(json_open)
    response_list = json_load["response"]

    for i in range(len(response_list)):
        if "items" in response_list[i]:
            for j in range(len(response_list[i]["items"])):
                link = response_list[i]['items'][j]['link']

                if "https://www.uta-net.com/song" in link or "https://www.uta-net.com/movie" in link:

                    if "https://www.uta-net.com/movie" in link:
                        link = link.replace('movie', 'song')

                    response = requests.get(link)

                    #オブジェクト生成
                    soup = BeautifulSoup(response.text, 'lxml')
                    singer_and_song = soup.find_all(id="ttl_name_box")
                    path = soup.find('input', id="linkcodebox")['value']
                    for tmp in singer_and_song:
                        tmp.text.strip("\n")

                    tmp_list = tmp.text.strip("\n").split("\n")

                    song = tmp_list[0]
                    print(tmp_list[0])
                    print(tmp_list[1])
                    output_lyrics(soup)

                    return

if __name__ == "__main__":

    main()

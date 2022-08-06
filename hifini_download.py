import re
import requests
from bs4 import BeautifulSoup
from hifi_search import searchMusic
from hifi_search import header


def downloadMusic():

    href_list ,keyword= searchMusic()

    while len(href_list) == 0:
        print("Cannot search what you have input! Please input again:")
        href_list ,keyword= searchMusic()

    first_res_hresf = href_list[0]

    url_download = "https://hifini.com/" + str(first_res_hresf)

    print("首选下载地址:" + url_download)

    seq = int(input("请选择下载地址——请输入序号:"))

    res_href = href_list[seq -1]

    url_download = "https://hifini.com/" + str(first_res_hresf)

    print("当前下载地址:" + url_download)

    res_download = requests.get(url=url_download, headers=header)

    # print(res_download.text)

    obj = re.compile(r"'(?P<getMusic>get_music.php.*?)'", re.S)

    getMusic = obj.finditer(res_download.text)

    getMusicUrl = ""

    for it in getMusic:
        # print(it.group('getMusic'))
        getMusicUrl = str(it.group('getMusic'))

    # print("getMusicUrl = " + getMusicUrl)

    downloadUrl = "https://hifini.com/" + getMusicUrl

    print("downloadUrl = " + downloadUrl)

    path = "./music/" + keyword + ".m4a"

    filename = keyword + ".m4a"

    print("path = " + str(path))

    res_music = requests.get(url=downloadUrl, headers=header)

    with open(path, mode="wb") as f:
        f.write(res_music.content)
        print("Download over!")
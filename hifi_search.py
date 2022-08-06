import re
import requests
from bs4 import BeautifulSoup

header = {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "cookie" : "bbs_sid=i179iueui659ofu5k6c5hf59j5; Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1659492665; bbs_token=_2FgCUfFWaNDv2GLO7j_2Fcm2_2B8oFjxugwvKQwf_2BVAkUl2mx_2FYjXv4XIgHAOUAo5oFIw11rnTo8GCacmG2C3O2YxEKQUyGHCA_2Byt; Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2=1659496418"
}

def searchMusic():
    keyword = str(input("请输入要搜索的内容:"))

    url_search = "https://hifini.com/search.htm?keyword=" + keyword

    

    # param = {
    #     "keyword" : "周杰伦" 
    # }

    res_search = requests.get(url=url_search, headers=header)

    # print(res_search.text)

    searchPage = BeautifulSoup(res_search.text, "html.parser")

    a = searchPage.find_all("a")

    obj = re.compile(r"<a href=\"(?P<href>thread-.*?htm)\"", re.S)

    li = list()

    cnt = 1
    for i in a:
        # print(str(i))
        res_href = obj.finditer(str(i))
        for it in res_href:
            print(str(cnt) + ":" + it.group('href'))
            li.append(it.group('href'))
            cnt += 1

    return li, keyword


import requests

url_login = "https://hifini.com/user-login.htm"

header = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

res_login = requests.get(url=url_login, headers=header)

print("Cookie of res_login : " + str(res_login.cookies))

# print(res_login.text)

url_vcode = "https://hifini.com/vcode.htm"

res_vcode = requests.get(url=url_vcode, headers=header)

print("Cookie of res_vcode :" + str(res_vcode.cookies))

with open("vcode.jpg", mode="wb") as f:
    f.write(res_vcode.content)


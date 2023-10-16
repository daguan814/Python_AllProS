import time
from datetime import datetime
import requests

base_url = "http://nsstudy.whttc.com/kj/ViewPlay.aspx?xl=1&id="
cookie = "TheMaxTime=16778.09; ASP.NET_SessionId=opm5itplnyw2x2hmbtute45r; SavedLogin=UserName=429006199109226325&Userid=13608"
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "__VIEWSTATE": "Bv7oslawzbwViMpWbGJyDrsCozTIdZ6xAnE9hXUtqPIdTJcqSAqbo6IAd3ZNqfSOo9Aiyw1aWIdzK2Q0xOh5qpJNy31+4C/QprrdhRCgKXh/cct7b7iVd0t69ub2xYxXgmTdyA==",
    "__VIEWSTATEGENERATOR": "5620F3FD",
    "__EVENTVALIDATION": "bZFEuCECcfe5gOCWabl77di99n/g7oAhzcmDVso4bQFvGM7EVGOccwpxLY24Qu3TKT8xNDHMIBe+4LneI1uVgtZmCNB6rxWVF5/nM90SMQEUZpYuB4GW6AYcBmJuyCteg6cGFopXORYauIVJbaa38ngWKB4=",
    "Button1": "Button",
}

for i in range(784, 796):
    time.sleep(1)
    true_url = base_url + str(i)
    print(true_url)
    response = requests.post(true_url, headers=headers, data=data)
    print(response.text)


# 获取当前时间字符串
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 获取Cookie字符串
cookie_str = headers.get("Cookie", "")

# 存储时间和Cookie字符串以及一个空行到log文件
with open("log.txt", "a") as log_file:
    log_file.write(f"Time: {current_time}\n")
    log_file.write(f"Cookie: {cookie_str}\n\n")

print("完成刷课！日志已存储")

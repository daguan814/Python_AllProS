'''
@Author 浊玉
@Description  
@Date create in 2023/8/22 23:53
'''


import requests


# 初始化cookie和token


class ZhiChu:
    def __init__(self, mon, day, Glo_Cookie, Glo_Token):
        self.day = day
        self.mon = mon
        self.Glo_Cookie = Glo_Cookie
        self.Glo_Token = Glo_Token

    # 支出请求发送
    def sendZhiReq(self, num):
        headers = {
            "Host": "www.yuxiaor.com",
            "Cookie": self.Glo_Cookie,
            "accept": "*/*",
            "user-agent": "YuxiaorReborn/9.5.2 (com.yuxiaor.Yuxiaor; build:8700; iOS 16.5.0) Alamofire/5.4.4",
            "xxx-yuxiaor-token": self.Glo_Token,
            "accept-language": "zh-Hans-CN;q=1.0"
        }
        # 设置查询的日期
        date = '2023-{}-{}'.format(self.mon, self.day)
        url = f"https://www.yuxiaor.com/api/v1/bill_logs"
        params = {
            "fromDate": date,
            "pageNum": num,
            "payType": 2,
            "pageSize": "30",
            "toDate": date
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()
        else:
            print("API request failed with status code:", response.status_code)
            print("Response content:", response.text)
        return json_data

    # 获取所有支出分页账单数据
    def fetch_all_bills(self):
        all_bills = []
        page_num = 1  # 从第一页开始获取
        while True:
            json_data = self.sendZhiReq(page_num)
            page_total = json_data.get('pageTotal', 0)
            bills = json_data.get('data', [])
            all_bills.extend(bills)
            page_num += 1
            if page_num > page_total:
                break
        return all_bills

    # 构建支出二维数组
    def build_Zhi_array(self):
        all_zhangdan = self.fetch_all_bills()
        count = len(all_zhangdan)  # 总账单条数（合并后的）
        print("总支出账单条数:", count)
        # 创建二维数组并存储所需字段
        Zhi_array = []
        for item in all_zhangdan:
            row = [item["payDateSStr"], item["address"], item["typeName"], item["absAmount"]]
            Zhi_array.append(row)
        # 将第三列包含押金的项改成"退押金"，包含租金的项改成"付租金"
        for item in Zhi_array:
            if '退' in item[2]:
                item[2] = '退押金'
            elif '租金' in item[2]:
                item[2] = '退押金'
        Zhi_array.insert(0, ['时间', '地址', '用途', '金额'])
        '''得到最终数组：zhichu_array'''
        return Zhi_array




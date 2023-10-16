'''
@Author 浊玉
@Description  
@Date create in 2023/8/15 20:20
'''

import requests


class ShouRu:
    def __init__(self, mon, day, Glo_Cookie, Glo_Token):
        self.day = day
        self.mon = mon
        self.Glo_Cookie = Glo_Cookie
        self.Glo_Token = Glo_Token

        # 收入请求发送

    def sendShouRuReq(self, num):
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
        url = f"https://www.yuxiaor.com/api/v1/bill_logs_detail_list"
        params = {
            "fromDate": date,
            "pageNum": num,
            "payType": 1,
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

    # 获取所有收入分页账单数据
    def fetch_all_bills(self):
        all_bills = []
        page_num = 1  # 从第一页开始获取
        while True:
            json_data = self.sendShouRuReq(page_num)
            page_total = json_data.get('pageTotal', 0)
            bills = json_data.get('data', [])
            all_bills.extend(bills)
            page_num += 1
            if page_num > page_total:
                break

        return all_bills

        # 构建收入二维数组

    def build_Shou_array(self):
        all_zhangdan = self.fetch_all_bills()
        count = len(all_zhangdan)  # 总账单条数（合并后的）
        print("总收入账单条数:", count)
        # 创建二维数组并存储所需字段
        Shou_array = []
        for item in all_zhangdan:
            row = [item["payDateSStr"], item["address"], item["amount"], item["feeTypeName"]]
            Shou_array.append(row)

        merged_data = {}  # 用于存储合并后的数据
        for row in Shou_array:
            date, address, amount, fee_type = row
            key = address.strip()  # 去除地址两端的空格
            if key not in merged_data:
                merged_data[key] = {
                    "日期": date,
                    "地址": address,
                    "水费金额": 0.0,
                    "物业费金额": 0.0,
                    "房租金额": 0.0,
                    "电费金额": 0.0,
                    "押金金额": 0.0,
                    "备注": "",
                }

            if '押金' in fee_type:
                merged_data[key]["押金金额"] += amount
            elif '物业' in fee_type:
                merged_data[key]["物业费金额"] += amount
            elif '网费' in fee_type:
                merged_data[key]["物业费金额"] += amount
            elif '保洁' in fee_type:
                merged_data[key]["物业费金额"] += amount
            elif '租' in fee_type:
                merged_data[key]["房租金额"] += amount
            elif '电费' in fee_type:
                merged_data[key]["电费金额"] += amount
            elif '水' in fee_type:
                merged_data[key]["水费金额"] += amount
        # 创建最终收入的二维数组
        shouru_array_final = [["日期", "地址", "水费金额", "物业费金额", "房租金额", "电费金额", "押金金额", "备注"]]

        # 填充合并后的数据到最终的二维数组
        for values in merged_data.values():
            merged_row = [
                values["日期"],
                values["地址"],
                values["水费金额"],
                values["物业费金额"],
                values["房租金额"],
                values["电费金额"],
                values["押金金额"],
                values["备注"],
            ]
            shouru_array_final.append(merged_row)
        return shouru_array_final




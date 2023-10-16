import json
import subprocess

# 提示用户输入自定义的月份和日期
custom_from_date = input("请输入起始日期（格式：YYYY-MM-DD）：")
custom_to_date = input("请输入结束日期（格式：YYYY-MM-DD）：")

# 构建自定义的 URL
url = (
    f"https://www.yuxiaor.com/api/v1/accountant/payments-report?"
    f"_defaultSelectId=214380&billType=0&dateType=1&departmentId=214380&departmentRouter=0-214380"
    f"&fromDate={custom_from_date}&houseBizType=0&pageNum=1&pageSize=30&payType=1&paymentStatus=2"
    f"&toDate={custom_to_date}"
)

# 使用 curl 获取 JSON 数据并通过管道传递给 jq 进行处理
curl_command = (
    f'curl -H "Host: www.yuxiaor.com" -H "Cookie: JSESSIONID=DF4A1B502CD038D1FE0F6573345AD7CB" '
    f'-H "accept: */*" -H "user-agent: YuxiaorReborn/9.5.2 (com.yuxiaor.Yuxiaor; build:8700; iOS 16.5.0) '
    f'Alamofire/5.4.4" -H "xxx-yuxiaor-token: YeNs7npLUac#VvojluRYArg#edyrK0tFtKM#Y2EAM2Ytk2I#Ydohq6_6fJI#671e714c-4d47-4c11-9baf-4b698a62c51f" '
    f'-H "accept-language: zh-Hans-CN;q=1.0" --compressed "{url}"'
)

jq_command = 'jq -r \'.data[] | "\(.estateName) \(.userName)"\''

# 运行 curl 命令并通过管道传递给 jq
process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE)
json_output, _ = process.communicate()

# 解析 JSON 数据并提取所需字段
data = json.loads(json_output)
print(data)
formatted_data = [f"{entry['payDate']}  {entry['addressFull']} {entry['userName']} {entry['typeStr']}" for entry in data['data']]
user_names = [entry['userName'] for entry in data['data']]

# 将输出保存到文件 "催租.txt"
with open("催租.txt", "w") as output_file:
    for entry in formatted_data:
        output_file.write(entry + "\n")

# 将所有 userName 保存到文件末尾
with open("催租.txt", "a") as output_file:
    output_file.write("\n".join(user_names) + "\n")

print("输出已保存到文件 \"催租.txt\"")

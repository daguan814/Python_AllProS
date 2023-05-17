'''
@Author 浊玉
@Description   电话簿
@Date create in 2023/5/12 13：50
'''
contacts = {}

# 添加联系人信息
def add_contact(name, phone, email, company):
    contacts[name] = {
        'phone': phone,
        'email': email,
        'company': company
    }
    print(f"成功添加联系人 {name}！")

# 查询联系人信息
def search_contact(name):
    if name in contacts:
        print(f"{name} 的联系方式如下：")
        print(f"电话：{contacts[name]['phone']}")
        print(f"邮箱：{contacts[name]['email']}")
        print(f"工作单位：{contacts[name]['company']}")
    else:
        print(f"没有找到联系人 {name}！")

# 删除联系人信息
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"成功删除联系人 {name}！")
    else:
        print(f"没有找到联系人 {name}！")

# 修改联系人信息
def modify_contact(name, phone=None, email=None, company=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if company:
            contacts[name]['company'] = company
        print(f"成功修改联系人 {name} 的信息！")
    else:
        print(f"没有找到联系人 {name}！")

# 输出所有联系人信息
def show_contacts():
    if len(contacts) == 0:
        print("通讯录为空！")
    else:
        print("所有联系人信息如下：")
        for name, info in contacts.items():
            print(f"{name}：电话：{info['phone']}，邮箱：{info['email']}，工作单位：{info['company']}")

# 测试
add_contact('张三', '123456789', 'zhangsan@example.com', 'ABC公司')
add_contact('李四', '987654321', 'lisi@example.com', 'XYZ公司')
search_contact('张三')
delete_contact('李四')
modify_contact('张三', phone='111111111', email='zhangsan@gmail.com')
show_contacts()

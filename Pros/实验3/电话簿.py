'''
@Author 浊玉
@Description   电话簿
@Date create in 2023/5/12 13：50
'''
address_book = {}


def add_contact():
    name = input("请输入姓名: ")
    phone = input("请输入电话号码: ")
    email = input("请输入电子邮件地址: ")
    company = input("请输入工作单位: ")

    contact = {'姓名': name, '电话号码': phone, '电子邮件地址': email, '工作单位': company}
    address_book[name] = contact

    print("联系人已添加。")


def search_contact(name):
    if name in address_book:
        contact = address_book[name]
        print("联系人信息:")
        print_contact(contact)
    else:
        print("未找到联系人。")


def delete_contact(name):
    if name in address_book:
        del address_book[name]
        print("联系人已删除。")
    else:
        print("未找到联系人。")


def modify_contact(name, **kwargs):
    if name in address_book:
        contact = address_book[name]
        for key, value in kwargs.items():
            contact[key] = value
        print("联系人已修改。")
    else:
        print("未找到联系人。")


def show_contacts():
    if len(address_book) > 0:
        print("所有联系人:")
        for name, contact in address_book.items():
            print_contact(contact)
    else:
        print("通讯录为空。")


def print_contact(contact):
    for key, value in contact.items():
        print(f"{key}: {value}")


# # 添加联系人
# add_contact()
# add_contact()
#
# # 查询联系人
# search_contact('张三')
#
# # 删除联系人
# delete_contact('李四')
#
# # 修改联系人
# modify_contact('张三', phone='111111111', email='zhangsan@gmail.com')
#
# # 显示所有联系人
# show_contacts()
def print_menu():
    print("电话簿程序操作面板")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 显示联系人列表")
    print("4. 删除联系人")
    print("5. 退出")


if __name__ == '__main__':
    print_menu()
    while True:
        choice = input("请输入您的选择（1-4）: ")
        if choice == "1":
            # print("您选择了添加联系人")
            add_contact()
        elif choice == "2":
            # print("您选择了查找联系人")
            a = str(input("请输入要查找联系人的名字："))
            search_contact(a)
        elif choice == "3":
            # print("您选择了显示联系人列表")
            show_contacts()
        elif choice == "4":
            # print("删除！")
            b = str(input("请输入要删除联系人的名字："))
            delete_contact(b)
        elif choice == "5":
            # print("推出！")
            break
        else:
            print("无效的选择，请重新输入。")

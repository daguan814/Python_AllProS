'''
@Author 浊玉
@Description  
@Date create in 2023/8/22 23:53
'''
from 房屋自动化.账单.Universal import buildXlsx
from 房屋自动化.账单.支出账单构建 import ZhiChu
from 房屋自动化.账单.收入账单构建 import ShouRu

# 待完成：1.将所有方法分开构建。2.支出应该只获取支出账单，收入只获取收入详细账单，收入不需要获取所有的账单
mon = str(input('请输入月份：'))
day = str(input('请输入日期：'))
# 初始化cookie和token
Glo_Cookie = "JSESSIONID=DF4A1B502CD038D1FE0F6573345AD7CB"
Glo_Token = "YeNs7npLUac#VvojluRYArg#edyrK0tFtKM#Y2EAM2Ytk2I#Ydohq6_6fJI#671e714c-4d47-4c11-9baf-4b698a62c51f"
# 调用支出类
zhichu = ZhiChu(mon, day, Glo_Cookie, Glo_Token)
# 调用收入类
shouru = ShouRu(mon, day, Glo_Cookie, Glo_Token)


# 构建两个工作表
buildXlsx(shouru.build_Shou_array(), "收入")
buildXlsx(zhichu.build_Zhi_array(), "支出")

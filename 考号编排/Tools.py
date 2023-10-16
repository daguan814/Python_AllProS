'''
@Author 浊玉
@Description  
@Date create in 2023/10/11 09:09
'''
import pandas as pd

from openpyxl import Workbook


class Tools:

    def __init__(self):
        return

    def find_first_stu(self, array, banji):  # 寻找学生的索引
        for i, row in enumerate(array):
            if row[0] == banji:
                return i
        return 9999

    def write_to_kaohao(self, A):  # 将考场表转换成考号表
        num_rows = len(A)
        num_cols = len(A[0])
        B = []
        for col in range(num_cols):
            for row in range(num_rows):
                if A[row][col] != 9999:
                    # 将行号和列号格式化成4位数的字符串
                    row_num_str = str(row + 1).zfill(2)
                    col_num_str = str(col + 1).zfill(2)
                    B.append([A[row][col], f"{col_num_str}{row_num_str}"])

        return B

    def save_to_excel(self, data, filename):  # 将二维列表保存为Excel
        # 创建一个Workbook对象
        wb = Workbook()
        # 获取默认的工作表
        ws = wb.active
        # 将数据逐行写入工作表
        for row in data:
            ws.append(row)
        # 保存文件
        wb.save(filename)

    def excel_to_2d_array(self, file_path):  # 将Excel变成二维列表
        # 读取Excel文件
        df = pd.read_excel(file_path)
        # 获取第一个表格的数据，转化为二维数组
        data = df.values.tolist()
        return data

    def remove_empty_first_column_rows(self, matrix):
        return [row for row in matrix if row[0].strip()]

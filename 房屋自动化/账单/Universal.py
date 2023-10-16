'''
@Author 浊玉
@Description  
@Date create in 2023/8/23 10:31
'''
import openpyxl


def buildXlsx(defArray, filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    array = defArray
    # 将数据写入工作表
    for row in array:
        new_row = []
        for cell in row:
            if isinstance(cell, (int, float)):
                if cell == 0:  # 将数值为0的单元格改为空单元格
                    new_row.append('')
                else:
                    new_row.append(cell)
            else:
                new_row.append(cell)
        sheet.append(new_row)

    # 指定文件路径
    file_path = "/Users/shuijing/Desktop/{}.xlsx".format(filename)

    # 保存工作簿到指定路径
    workbook.save(file_path)

    print("Excel 文件已保存到指定路径:", file_path)

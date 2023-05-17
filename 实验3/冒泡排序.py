'''
@Author 浊玉
@Description  冒泡排序
@Date create in 2023/5/12 12:37
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 内层循环用于遍历未排序的部分，每次将最大的数移动到最后
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 测试代码
arr = [5, 2, 8, 4, 7, 1, 3, 6]
bubble_sort(arr)
print("排序后的结果为：", arr)

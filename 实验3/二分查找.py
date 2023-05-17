'''
@Author 浊玉
@Description  二分查找
@Date create in 2023/5/12 12:45
'''


#折半查找算法，查找前需要先排序
def binary_search(arr, target):
    # 初始化查找区间
    left = 0
    right = len(arr) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2  # 计算中位数
        count += 1

        if arr[mid] == target:
            return mid, count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, count


'''--------------------------------------------------'''
'''递归法二分查找'''
def binary_search_recursive(arr, target, left, right):
    # 查找区间已经为空，目标元素不存在
    if left > right:
        return -1, 0

    # 计算中位数
    mid = (left + right) // 2

    if arr[mid] == target:
        # 找到目标元素，返回下标和查找次数
        return mid, 1
    elif arr[mid] < target:
        # 目标元素在右侧区间，递归查找右侧区间
        index, count = binary_search_recursive(arr, target, mid+1, right)
        return index, count+1
    else:
        # 目标元素在左侧区间，递归查找左侧区间
        index, count = binary_search_recursive(arr, target, left, mid-1)
        return index, count+1

# 测试代码
arr = [1, 3, 4, 6, 7, 8, 10, 13, 15]
target = 7  #这里是要查找的元素，直接赋值
index, count = binary_search(arr, target)
if index != -1:
    print("要查找的元素 %d 存在，下标为 %d，一共查找了 %d 次。" % (target, index, count))
else:
    print("要查找的元素 %d 不存在，一共查找了 %d 次。" % (target, count))

'''递归二分查找测试代码'''
# arr = [1, 3, 4, 6, 7, 8, 10, 13, 15]
# target = 7
# index, count = binary_search_recursive(arr, target, 0, len(arr)-1)
# if index != -1:
#     print("要查找的元素 %d 存在，下标为 %d，一共查找了 %d 次。" % (target, index, count))
# else:
#     print("要查找的元素 %d 不存在，一共查找了 %d 次。" % (target, count))
#


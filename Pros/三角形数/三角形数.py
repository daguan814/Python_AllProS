'''
@Author 浊玉
@Description  
@Date create in 2023/6/6 21:07
'''

zhengchu = []
a = 1
sum = 0
while True:
    sum = a + sum
    a += 1
    # print(sum)
    if sum % 3 == 0:
        zhengchu.append(sum)
    if len(zhengchu) == 33:
        print(zhengchu)
        print(zhengchu[32])
        break

# ---coding = utf - 8--
# @Time : 2021/11/14 14:23
# @Author : 达观
# @File : change.py
# @function :
import time

import pyautogui
from pynput.mouse import Button, Controller as c_mouse

mouse = c_mouse()

pyautogui.PAUSE = 2  # 每个指令停顿两秒


def mouseClick(clickTimes, lOrR, img):
    x = 1
    while x <= 15:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            break
        x += 1
        print("未找到匹配图片,1秒后重试")
        time.sleep(1)


def startDo():  #坐标可以使用sni 获取
    time.sleep(4)
    mouseClick(1, 'left', '/Volumes/细雨带风/ROOT_Code/个人代码库/Python/基本代码库(爬虫)/自动办公/自动化/img/121.png') #这个是绝对路径
    mouse.click(Button.left, 2)  # 鼠标双击
    time.sleep(3)
    pyautogui.click(1759, 11)  # 控制中心
    time.sleep(1.5)
    pyautogui.click(1760, 360)  # 音乐和视频控制
    pyautogui.click(1621, 107)  # 开始按钮
    pyautogui.dragRel(266, button='left')  # 左键拖动
    pyautogui.click(1223, 308)  # 关闭播放窗口
    pyautogui.click(144, 145)  # 刷新课程状况
    time.sleep(3)
    pyautogui.click(960, 571)  # 点击确认按钮


if __name__ == '__main__':
    print('START')
    time.sleep(2)
    for xxxx in range(18):  # 这个里面填要点击的次数 这个次数是一页的
        startDo()


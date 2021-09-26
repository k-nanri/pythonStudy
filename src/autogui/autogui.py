import pyautogui
import time
from selenium import webdriver

if __name__ == '__main__':

    '''
    # マウス座標を(x, y)まで移動
    pyautogui.moveTo(100, 100)

    # sleep 3sec
    time.sleep(3)

    # マウスを(x,y)だけ移動
    pyautogui.moveRel(10, 10)

    # 現在の位置(x, y)を取得
    print(pyautogui.position())
    '''

    # Chromeを起動
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.co.jp")
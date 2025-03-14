import pyautogui
import cv2
import numpy as np
import time
import random
import os
import sys
import subprocess

# Function to install required packages
def install_packages():
    try:
        import pyautogui
        import cv2
        import numpy as np
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui', 'opencv-python', 'numpy'])

install_packages()

# Constants
RESOURCES_PATH = 'D:/脚本/resources/'
MAX_RECOGNITION_TIME = 10

# Helper functions
def display_message(message):
    pyautogui.alert(message, title='命运2自动脚本')

def find_image(image_path, timeout=MAX_RECOGNITION_TIME):
    start_time = time.time()
    while time.time() - start_time < timeout:
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        template = cv2.imread(image_path, 0)
        result = cv2.matchTemplate(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            return max_loc
    return None

def move_and_click(image_path):
    location = find_image(image_path)
    if location:
        pyautogui.moveTo(location[0] + 15, location[1] + 15)  # Adjusting for center of the image
        pyautogui.click()
        return True
    else:
        display_message("图像识别失败: " + image_path)
        return False

def random_wait(min_seconds, max_seconds):
    time.sleep(random.uniform(min_seconds, max_seconds))

def check_similarity(image_path1, image_path2, threshold=0.6):
    img1 = cv2.imread(image_path1, 0)
    img2 = cv2.imread(image_path2, 0)
    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val >= threshold

# Main script
while True:
    # Step 1: Set focus on the Destiny 2 game
    pyautogui.hotkey('alt', 'tab')
    display_message("步骤1: 聚焦到《命运2》游戏程序")

    # Step 2: Open the map and navigate to the City of Saints
    pyautogui.press('m')
    if not move_and_click(RESOURCES_PATH + '圣城字样.jpg'):
        continue
    if not move_and_click(RESOURCES_PATH + '幽冥探索图标.jpg'):
        continue
    if not move_and_click(RESOURCES_PATH + '幽冥探索图标2.jpg'):
        continue
    display_message("步骤2: 导航到圣城并进入幽冥探索")

    # Step 3: Wait for a random duration
    random_wait(2, 6)
    display_message("步骤3: 随机等待二到六秒")

    # Step 4: Find the start icon and click it
    if not move_and_click(RESOURCES_PATH + '开始字样.jpg'):
        continue
    display_message("步骤4: 点击开始")

    # Step 5: Wait for a random duration
    random_wait(20, 30)
    display_message("步骤5: 随机等待二十到三十秒")

    # Step 6: Compare the images
    if not check_similarity(RESOURCES_PATH + '当前地图.jpg', RESOURCES_PATH + '折磨者地图.jpg'):
        # Step 7: If similarity is low, restart
        pyautogui.press('tab')
        pyautogui.keyDown('o')
        time.sleep(5)
        pyautogui.keyUp('o')
        time.sleep(10)
        continue
    display_message("步骤6: 地图相似性检查通过")

    # Step 8: Navigate to the resource icon
    pyautogui.rightClick()
    if not move_and_click(RESOURCES_PATH + '资源图标.jpg'):
        continue
    pyautogui.rightClick()
    display_message("步骤8: 导航到资源图标")

    # Step 9: Move to the resource location
    pyautogui.keyDown('w')
    pyautogui.press('shift')
    while not move_and_click(RESOURCES_PATH + '资源采集图标.jpg'):
        pyautogui.press('space')
        time.sleep(1)
    pyautogui.keyUp('w')
    display_message("步骤9: 移动到资源采集位置")

    # Step 10: Interact with the resource
    pyautogui.keyDown('f')
    time.sleep(5)
    pyautogui.keyUp('f')
    display_message("步骤10: 采集资源")

    # Step 11: Wait for a random duration
    random_wait(3, 8)
    display_message("步骤11: 随机等待三到八秒")

    # Step 12: Restart the loop
    display_message("步骤12: 循环开始")
import pyautogui
import keyboard
import time

# クリック間の遅延時間（秒）
delay_between_clicks = 0.001

print("プログラムを終了するには、いつでも 'Ctrl + C' を押してください。")

try:
    while True:
        # F19キーが押されているかをチェック
        if keyboard.is_pressed('f19'):
            # F19キーが押されている間、マウスの左クリックを実行
            pyautogui.click()
        else:
            # キーが押されていない時は少し待機してから再チェック
            time.sleep(0.1)
except KeyboardInterrupt:
    print("プログラムが終了しました。")
import cv2
from datetime import datetime
import time
import ASUS.GPIO as GPIO
import os

camera_ch = 5  # 5 for Tinkerboard with 1 camera
camera = cv2.VideoCapture(camera_ch)

month = input("month:")
day = input("day")
hour = input("hour")

set_time = month + "/" + day + "-" + hour
print("set time is ")
print(set_time)
# ファイル保存用の設定
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))  # カメラの横幅を取得
h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # カメラの縦幅を取得

# フォルダ作成
start = input("first sample number")
end = input("last sample number")

for i in range(start, end):
    dir_pass = "/home/saku/data/" + str(i)
    os.mkdir(dir_pass)

GPIO.setmode(GPIO.ASUS)

StepPins = [73, 74, 8, 120]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]  # half
# seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] #wave
stepcount = len(seq)
stepcounter = 0
stepdir = 1
stepinitial = 0


def setpos(pos):
    pos = float(pos) / 360 * 4096
    if pos > 0:
        stepcount = len(seq)
        stepcounter = 0
        stepdir = 1
        stepinitial = 0

    else:
        stepcounter = len(seq) - 1
        stepcount = -1
        stepdir = -1
        stepinitial = stepcounter

    for i in range(0, abs(int(pos))):
        for j in range(0, 4):
            pinx = StepPins[j]
            if seq[stepcounter][j] == 1:
                GPIO.output(pinx, True)
            else:
                GPIO.output(pinx, False)

        stepcounter += stepdir
        if stepcounter == stepcount:
            stepcounter = stepinitial

        time.sleep(0.005)


while True:
    ret, frame = camera.read()  # フレームを取得
    cv2.imshow("camera", frame)  # フレームを画面に表示
    for i in range(1, 10):
        pos = -44
        now = datetime.now()
        now = now.strftime("%Y:%m:%d:%H:%M:%S")
        ret, frame = camera.read()  # フレームを取得
        fname = "/home/saku/data/" + str(i) + "/" + now + "-" + str(i) + ".jpg"
        cv2.imwrite(fname, frame)
        print(fname)
        if i == 9:
            pos = 352
        setpos(pos)
        time.sleep(1)

    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if now == set_time:
        break


# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()


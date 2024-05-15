import cv2

channel = 5  # カメラのチャンネル
cap = cv2.VideoCapture(channel)

while True:
    # カメラからの画像取得
    ret, frame = cap.read()

    # カメラの画像の出力
    cv2.imshow("camera", frame)

    # 繰り返し分から抜けるためのif文 escで脱出
    key = cv2.waitKey(10)
    if key == 27:
        break

# メモリを解放して終了するためのコマンド
cap.release()
cv2.destroyAllWindows()

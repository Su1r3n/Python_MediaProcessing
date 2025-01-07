import cv2
import os

dir_path = "videos/"
files = os.listdir(dir_path)

for i in range(len(files)):
    filepath = dir_path + str(files[i])
    root, ext = os.path.splitext(filepath)
    if (ext == ".mp4" ) or (ext == ".MP4"):
        os.makedirs("images/" + str(os.path.splitext(os.path.basename(filepath))[0]), exist_ok=True)
        capture = cv2.VideoCapture(filepath) 
        fps = int(capture.get(cv2.CAP_PROP_FPS))
        count = 0  # フレーム用カウンタ
        while True:
            ret, frame = capture.read()
            if not ret:  # 読み込めなかった場合はループを抜ける
                break
            if int(count % fps) == 0:  # 1秒ごとにフレームを保存
                cv2.imwrite("images/" + os.path.splitext(os.path.basename(filepath))[0] + "/"+ str(count) + ".png", frame)
            count += 1
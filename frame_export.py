import cv2
import os

dir_path = "videos/"    #path指定
files = os.listdir(dir_path)    #ディレクトリ内のファイルをみる

for i in range(len(files)):
    filepath = dir_path + str(files[i])
    os.makedirs("images/" + str(os.path.splitext(os.path.basename(filepath))[0]), exist_ok=True)    #書き出した後のフォルダ作成
    capture = cv2.VideoCapture(filepath)  #動画を読み込む
    fps = int(capture.get(cv2.CAP_PROP_FPS))    #動画のfpsをみる
    count = 0  # フレーム用カウンタ
    while True:
        ret, frame = capture.read()
        if not ret:  # 読み込めなかった場合はループを抜ける
            break
        if int(count % fps) == 0:  # 1秒ごとに
            cv2.imwrite("images/" + os.path.splitext(os.path.basename(filepath))[0] + "/"+ str(count) + ".png", frame)  #画像を保存
        count += 1
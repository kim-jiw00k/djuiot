import serial
import tkinter as tk
from PIL import Image, ImageDraw, ImageGrab
import cv2 as cv
import keras
import threading

def paint( event ):
    x1, y1 = (event.x -1), (event.y -1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_rectangle(x1, y1, x2, y2, fill="black",width=8)   # 선을 사각형으로 만들며 굵기는 8이다.

    # 이미지에 그리기
    draw.rectangle([x1, y1, x2, y2], fill="black",width=8)      # 이미지에도 만들어서 저장하는 용도

def save_image():
    # 캔버스의 내용을 이미지로 저장
    x = win.winfo_rootx() + canvas.winfo_x()    # 전체 화면에서 캔버스의 x 좌표 계산
    y = win.winfo_rooty() + canvas.winfo_y()    # 전체 화면에서 캔버스의 y 좌표 계산
    x1 = x + canvas.winfo_width()               # 화면을 움직여도 화면을 따라가서 저장함
    y1 = y + canvas.winfo_height()              # 화면을 움직여도 화면을 따라가서 저장함

    # 캔버스의 내용을 이미지로 캡처
    ImageGrab.grab().crop((x, y, x1, y1)).save("test.jpg")      # 캡쳐 후 test.jpg로 저장
    print('사진이 저장 되었습니다.')

    # 필기체를 인식하는 모델을 사용하여 아두이노로 출력

    test_model = keras.models.load_model("CNN_MNIST_Model_ver2.keras")  # epochs 50번 돌린 모델 정확도 98%

    Original = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
    image = cv.resize(Original, (28, 28))
    image = 255 - image
    image = image.astype('float32')
    image = image.reshape(-1, 28, 28, 1)  # 평탄화
    image = image / 255.0  # 예측할 이미지

    predict_image = test_model.predict(image)
    predict_image_argmax = predict_image.argmax()
    print(f"추정된 숫자 : {predict_image_argmax}")  # 숫자가 복잡해서 가장 큰 값만 뽑아옴
    ser.write(str(predict_image_argmax).encode('utf-8'))  # 시리얼 포트로 추정된 숫자 전송
    # predict_image_argmax값을 문자열로 변환


def serial_read():
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received data : {data}")
        except Exception as e:
            print(f"Serial read error {e}")
            break # 시리얼 포트 읽다가 오류가 나면 종료

ser = serial.Serial(port='COM3', baudrate=115200, timeout=2)


win = tk.Tk()
win.title("마우스로 그림 그리기")

canvas = tk.Canvas(win, width=300,height=300,bg='white')
canvas.pack(fill= 'both', expand= True)
canvas.bind("<B1-Motion>", paint)
save_button = tk.Button(win, text='저장', command=save_image)     # 저장 버튼
save_button.pack()


image = Image.new("RGB", (300,300), "white")
draw = ImageDraw.Draw(image)


message = tk.Label(win, text="마우스를 자유롭게 그림을 그려보세요")
message.pack(side=tk.BOTTOM)

# thread 를 만든다.
thread = threading.Thread(target=serial_read, daemon=True)
thread.start()

win.mainloop()
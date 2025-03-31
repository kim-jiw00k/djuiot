import serial
import tkinter as tk
from PIL import Image, ImageDraw, ImageGrab

def paint( event ):
    x1, y1 = (event.x -1), (event.y -1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    # 이미지에 그리기
    draw.rectangle([x1, y1, x2, y2], fill="black")

def save_image():
    # 캔버스의 내용을 이미지로 저장
    x = win.winfo_rootx() + canvas.winfo_x()    # 전체 화면에서 캔버스의 x 좌표 계산
    y = win.winfo_rooty() + canvas.winfo_y()    # 전체 화면에서 캔버스의 y 좌표 계산
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # 캔버스의 내용을 이미지로 캡처
    ImageGrab.grab().crop((x, y, x1, y1)).save("test.jpg")
    print('사진이 저장 되었습니다.')

ser = serial.Serial(port='COM3', baudrate=115200, timeout=2)


win = tk.Tk()
win.title("마우스로 그림 그리기")

canvas = tk.Canvas(win, width=300,height=300,bg='white')
canvas.pack(fill= 'both', expand= True)
canvas.bind("<B1-Motion>", paint)
save_button = tk.Button(win, text='저장', command=save_image)
save_button.pack()

image = Image.new("RGB", (300,300), "white")
draw = ImageDraw.Draw(image)


message = tk.Label(win, text="마우스를 자유롭게 그림을 그려보세요")
message.pack(side=tk.BOTTOM)

win.mainloop()
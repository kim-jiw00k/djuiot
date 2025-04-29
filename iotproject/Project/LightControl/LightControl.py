import RPi.GPIO as GPIO         #파이썬에서 LED 제어를 위한 참조
import paho.mqtt.client as mqtt #MQTT 통신을 위한 참조

GPIO.setwarnings(False)         # 오류 나는걸 방지
GPIO.setmode(GPIO.BOARD)        # BOARD 방식으로 연결

GPIO.setup(11,GPIO.OUT)         # 11번 출력
GPIO.setup(12,GPIO.OUT)         # 12번 출력
GPIO.setup(13,GPIO.OUT)         # 13번 출력

BROKER_IP = "192.168.0.5"       # 라즈베리파이 IP
BROKER_PORT = 1883              # 포트번호
TOPIC = "LightControl"          # 토픽 이름

power = False                   # 색상 선택을 위한 power 전역 변수

def on_msg(client, userdata, msg):
    global power                # 전역 변수 선언
    message = msg.payload.decode()
    print("Receive msg : ",message)
    if message == "ON":         # ON 일때 기본 값 다 켜짐
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        power = True            # power는 True가 됨
    
    elif message == "OFF":      # OFF 일때 모두 꺼짐
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        power = False           # power False가 됨
    
    if power == True:           # 전구가 켜져 있을 때
        if message == "R":      # R 이 들어오면 R 빼고 다 꺼짐 빨간색
            GPIO.output(11, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
        elif message == "G":    # G 가 들어오면 G 빼고 다 꺼짐 초록색
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
        elif message == "B":    # B가 들어오면 B 빼고 다 꺼짐 파란색
            GPIO.output(11, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)



client = mqtt.Client()          # 클라이언트 객체 생성 서버와 연결, 메세지 송수신
client.on_message = on_msg      # 메세지 수신 시 실행할 콜백 함수등록

client.connect(BROKER_IP, BROKER_PORT)  # MQTT 브로커 서버에 연결 192.168.0.5:1883 에 연결
client.subscribe(TOPIC) # 특정 토픽을 구독 LightControl 에 구독

try:
    client.loop_forever()   # 메세지를 계속 수신 대기 시킴 이 루프가 있어야 메세지 수신 가능
except KeyboardInterrupt:       #ctrl+C 를 누르면 꺼짐
    print("Program End")
    GPIO.cleanup()          # 사용한 핀을 초기화 다른 프로그램과 충돌 방지

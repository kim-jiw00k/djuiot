import RPi.GPIO as GPIO         # 파이썬에서 LED 제어를 위한 참조
import paho.mqtt.client as mqtt # MQTT 통신을 위한 참조

GPIO.setwarnings(False)         # 오류 나는걸 방지
GPIO.setmode(GPIO.BOARD)        # BOARD 방식으로 연결

GPIO.setup(11,GPIO.OUT)         # 11번 출력 R
GPIO.setup(12,GPIO.OUT)         # 12번 출력 G
GPIO.setup(13,GPIO.OUT)         # 13번 출력 B

# 밝기를 위한 핀 출력 설정
red_pwm = GPIO.PWM(11, 100)
green_pwm = GPIO.PWM(12, 100)
blue_pwm = GPIO.PWM(13, 100)

# 초기 상태 0 으로 설정
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

BROKER_IP = "192.168.0.5"       # 라즈베리파이 IP
BROKER_PORT = 1883              # 포트번호
TOPIC = "LightControl"          # 토픽 이름

power = False                   # 색상 선택을 위한 power 전역 변수
current_color = "OFF"           # 밝기를 위해 현재 색상을 정함
brightness = 100                # 기본 밝기 100

# 밝기 적용 함수
def brightness_apply():
    if not power:                   # power 가 false 일 때 만 실행
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(0)
    elif current_color == "R":
        red_pwm.ChangeDutyCycle(brightness)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(0)
    elif current_color == "G":
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(brightness)
        blue_pwm.ChangeDutyCycle(0)
    elif current_color == "B":
        red_pwm.ChangeDutyCycle(0)
        green_pwm.ChangeDutyCycle(0)
        blue_pwm.ChangeDutyCycle(brightness)
    elif current_color == "ON":
        red_pwm.ChangeDutyCycle(brightness)
        green_pwm.ChangeDutyCycle(brightness)
        blue_pwm.ChangeDutyCycle(brightness)

# 메세지 수신 처리
def on_msg(client, userdata, msg):
    global power, current_color, brightness                # 전역 변수 선언
    message = msg.payload.decode()
    print("Receive msg : ",message)
    
    if message == "ON":         # ON 일때 기본 값 다 켜짐
        current_color = "ON"
        power = True            # power는 True가 됨
        brightness_apply()
    
    elif message == "OFF":      # OFF 일때 모두 꺼짐
        current_color = "OFF"
        power = False           # power False가 됨
        brightness_apply()
    
    elif message in ["R", "G", "B"]:    # R,G,B 라고 메세지가 왔을 때
        if power:                       # power가 true 일 때
            current_color = message     # 색상을 메세지대로 바꾸고
            brightness_apply()          # 함수를 이용해서 색의 밝기를 적용
            
    elif message.startswith("BRIGHTNESS:"): #BRIGHTNESS: 라는 문자열이 들어오면
        try:
            value = int(message.split(":")[1]) # value 에다가 : 뒤에 문자열을 int형으로 변환 하여 저장
            brightness = value                 # value 를 brightness에 저장하여 밝기 조절
            if power:
                brightness_apply()
        except:
            pass

client = mqtt.Client()          # 클라이언트 객체 생성 서버와 연결, 메세지 송수신
client.on_message = on_msg      # 메세지 수신 시 실행할 콜백 함수등록

client.connect(BROKER_IP, BROKER_PORT)  # MQTT 브로커 서버에 연결 192.168.0.5:1883 에 연결
client.subscribe(TOPIC) # 특정 토픽을 구독 LightControl 에 구독

try:
    client.loop_forever()   # 메세지를 계속 수신 대기 시킴 이 루프가 있어야 메세지 수신 가능
except KeyboardInterrupt:       #ctrl+C 를 누르면 꺼짐
    print("Program End")
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()          # 사용한 핀을 초기화 다른 프로그램과 충돌 방지

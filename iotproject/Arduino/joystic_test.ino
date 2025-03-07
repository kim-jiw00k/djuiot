#include <Servo.h>
#include <DHT.h>

#define DHTTYPE DHT11

Servo myServer;

//joystick
int gndjPin = A0;
int vccjPin = A1;
int xPin = A2;
int yPin = A3;
int swPin = A4;
//부저
int buzPin = 4;
//울트라
int triggerPin = 5;
int echoPin = 6;
//서보
int servo = 7;
//온습도
int dhtPin = 3;
DHT dht(dhtPin, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(gndjPin, OUTPUT);     //조이스틱 용
  pinMode(vccjPin, OUTPUT);     //조이스틱 용
  pinMode(xPin, INPUT);         //조이스틱 용
  pinMode(yPin, INPUT);         //조이스틱 용
  pinMode(swPin, INPUT_PULLUP); //조이스틱 용
  pinMode(echoPin, INPUT);      //울트라 용
  pinMode(triggerPin, OUTPUT);  //울트라 용
  digitalWrite(gndjPin, LOW);   //조이스틱 용
  digitalWrite(vccjPin, HIGH);  //조이스틱 용
  myServer.attach(servo);       //서보 용
  //pinMode(dhtPin, INPUT);      //온/습도
  dht.begin();                  //온/습도
}

void loop() {
  int x = map(analogRead(xPin), 0, 1023, -5, 5);
  int y = map(analogRead(yPin), 0, 1023, -5, 5);
  if(x > 0 && y == 0) //right
  {
    ultra1();
  } 
  else if (x < 0 && y == 0) //left
  {
    buzzer1();
  }
  else if (x == 0 && y > 0) // down
  {
    servo1();
  }
  else if (x == 0 && y < 0) // up
  {
    temper1();
  }
  delay(500);
}

void ultra1()  //후방 감지
{
  float fDuration, fDistance;

  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  fDuration = pulseIn(echoPin, HIGH);
  fDistance = ((float)(340 * fDuration) / 10000) / 2;
  delay(250);
  Serial.print(fDistance);
  if(fDistance < 30)
  {
    tone(buzPin,523,250);
    delay(1000);
    if(fDistance < 20)
    {
      noTone(buzPin);
      tone(buzPin,523,250);
      delay(500);
      if(fDistance < 10)
      {
        noTone(buzPin);
        tone(buzPin,523,250);
        delay(400);
        if(fDistance < 5)
        {
          noTone(buzPin);
          tone(buzPin,523,250);
          delay(250);
        }
      }
    }
  }
}

void buzzer1()
{
  tone(buzPin, 392, 250); //솔
  Serial.println("부저");
}

void temper1()
{
  delay(2000);
  float fTemp = dht.readTemperature();
  float fHumi = dht.readHumidity();

  if(isnan(fTemp) || isnan(fHumi))
  {
    Serial.println("Failed to read from DHT");
    return;
  }
  Serial.print("온도 : ");
  Serial.print(fTemp);
  Serial.println("[C]\t");
  Serial.print("습도 : ");
  Serial.print(fHumi);
  Serial.println("[C]\t");
  Serial.println("온/습도");
}

void servo1()
{
  myServer.write(0);
  delay(1000);
  myServer.write(90);
  delay(1000);
  myServer.write(180);
  delay(1000);
  Serial.println("서보");
}
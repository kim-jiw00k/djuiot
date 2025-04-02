int pin[7]={8,7,6,5,4,3,2}; // 8:A,7:B,6:C,5:D,4:E,3:F,2:G
int S1 = 9;                 // DP

void setup() {
  // put your setup code here, to run once:
  for(int i = 2; i<9; i++)
  {
    pinMode(i, OUTPUT);
  }
  pinMode(S1, OUTPUT);
  digitalWrite(S1,HIGH);
  Serial.begin(115200UL);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    String data = Serial.readString();
    if (data.equals("1"))
    {
      digitalWrite(8, HIGH);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(2, HIGH);
      Serial.println(F("Number : 1"));
    }
    else if (data.equals("2"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, HIGH);
      digitalWrite(5, LOW);
      digitalWrite(4, LOW);
      digitalWrite(3, HIGH);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 2"));
    }
    else if (data.equals("3"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 3"));
    }
    else if (data.equals("4"))
    {
      digitalWrite(8, HIGH);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 4"));
    }
    else if (data.equals("5"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 5"));
    }
    else if (data.equals("6"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, LOW);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 6"));
    }
    else if (data.equals("7"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(2, HIGH);
      Serial.println(F("Number : 7"));
    }
    else if (data.equals("8"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, LOW);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 8"));
    }
    else if (data.equals("9"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, HIGH);
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      Serial.println(F("Number : 9"));
    }
    else if (data.equals("0"))
    {
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);
      digitalWrite(5, LOW);
      digitalWrite(4, LOW);
      digitalWrite(3, LOW);
      digitalWrite(2, HIGH);
      Serial.println(F("Number : 0"));
    }
  }
}
 
package com.example.project1_smart_light_control;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttMessage;



public class MainActivity extends AppCompatActivity {

    private static final String ServerIP = "tcp://192.168.0.5:1883";   // 서버 아이피
    private static final String TOPIC = "LightControl";    // 토픽
    private MqttClient mqttClient; // MQTT 클라이언트

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        try {
            mqttClient = new MqttClient(ServerIP, MqttClient.generateClientId(), null); // 3번 연결설정
            mqttClient.connect();

            if (mqttClient.isConnected()){
                Log.d("MQTT", "연결 성공");
            }else {
                Log.d("MQTT", "연결 실패");
            }


            mqttClient.subscribe(TOPIC); // 5번 구독 설정
            mqttClient.setCallback(new MqttCallback() { // 6번 콜백 설정
                @Override
                public void connectionLost(Throwable cause) {
                    Log.d("MQTT", "연결 실패");
                }

                @Override
                public void messageArrived(String topic, MqttMessage message) throws Exception {
                    Log.d("MQTT", "메세지 도착 : " + message.toString()); // 7번 메세지 도착
                }

                @Override
                public void deliveryComplete(IMqttDeliveryToken token) {
                    Log.d("MQTT", "전달 완료");
                }
            });
        } catch (Exception e) {
            Log.e("MQTT", "에러", e);
        }
        // 전구 ON 기본 값은 다 켜짐
        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button sendonButton = findViewById(R.id.btn_on);
        sendonButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("MQTT", "전송");
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("ON".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        // 전구 OFF
        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button sendoffButton = findViewById(R.id.btn_off);
        sendoffButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("MQTT", "전송");
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("OFF".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        // 색상 변경 RED
        Button Redbtn = findViewById(R.id.btn_red);
        Redbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("R".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        // 색상 변경 GREEN
        Button Greenbtn = findViewById(R.id.btn_green);
        Greenbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("G".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        // 색상 변경 BLUE
        Button Bluebtn = findViewById(R.id.btn_blue);
        Bluebtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("B".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

        Button bright25 = findViewById(R.id.lightnessctl25);
        bright25.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("BRIGHTNESS:25".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button bright50 = findViewById(R.id.lightnessctl50);
        bright50.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("BRIGHTNESS:50".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button bright75 = findViewById(R.id.lightnessctl75);
        bright75.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("BRIGHTNESS:75".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button bright100 = findViewById(R.id.lightnessctl100);
        bright100.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    mqttClient.publish(TOPIC, new MqttMessage("BRIGHTNESS:100".getBytes())); // 4번 메세지 전송
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

    }
}

package com.example.button;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {           //메인 화면
    private TextView textView;          //TextView 타입 객체 textView 선언

    @Override
    protected void onCreate(Bundle savedInstanceState) {        // 화면 생성 이벤트
        super.onCreate(savedInstanceState);                     // 부모 생성자 호출
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);                 // 메인 화면 표시
        // xml의 TextView 위젯을 연결한다.
        textView = (TextView) findViewById(R.id.textView);
        // xml의 Button 위젯을 연결한다.
        //Button 타입 객체 button 선언
        Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textView.setText("잘가시게~");
            }
        });

    }
}

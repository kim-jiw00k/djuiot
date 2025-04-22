package com.example.edittext;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    /* 멤버변수는 속성을 나타내는데 기본적으로 외부의 접근을 차단하기 위해 private 접근제한자를 사용한다.*/
    private TextView textView;      // 멤버 변수
    private Button bt;              // 멤버 변수
    private EditText ed;            // 멤버 변수
    // 멤버함수는 외부에서 접근을 위하여 public 접근 제한자를 사용한다.
    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {        // 화면 생성 이벤트
        super.onCreate(savedInstanceState);                     // 부모 생성자 호출
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);                 // 메인 화면을 표시
        textView = (TextView) findViewById(R.id.tv);
        bt = (Button) findViewById(R.id.bt);
        ed = (EditText) findViewById(R.id.edtv);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = ed.getText().toString();
                ed.setText("");
                textView.setText(str);
            }
        });

    }
}
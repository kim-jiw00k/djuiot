package com.example.application2;

import android.app.Application;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class main_apllication2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_apllication2);

        EditText et = (EditText) findViewById(R.id.et);
        Button btn = (Button) findViewById(R.id.bt);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String id = et.getText().toString();                // editText에 입력된 id 저장
                Application application = getApplication();         // Application 접근
                MyApplication myApp = (MyApplication) application;  // Application --> MyApplication 변환
                myApp.setId(id);

                Intent intent = new Intent(main_apllication2.this, sub_application2.class);
                startActivity(intent);
            }
        });
    }
}
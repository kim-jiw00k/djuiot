package com.example.datatransfer;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class Subdatatransfer extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_subdatatransfer);

        // 전달된 인텐트를 복사해서 인텐트 객체 생성
        Intent intent = getIntent();
        String msg = intent.getStringExtra(Maindatatransfer.TAG_MSG);
        TextView tv2 = (TextView) findViewById(R.id.sub_tv);
        tv2.setText(msg);
    }
}
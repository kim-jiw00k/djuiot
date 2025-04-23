package com.example.application2;

import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class sub_application2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_sub_application2);

        MyApplication myApplication = (MyApplication) getApplication();
        String id = myApplication.getId();  // Myapplication의 getId()로 ID를 가져온다.
        TextView tv = (TextView) findViewById(R.id.sub_tv);
        tv.setText(id);
    }
}
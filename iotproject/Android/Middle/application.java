package com.example.application;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class application extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_application);

        MyApplication myApplication = (MyApplication) getApplication();
        String getStr = myApplication.getGlobalstr();

        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        TextView tV = (TextView) findViewById(R.id.tv);
        tV.setText(getStr);

    }
}
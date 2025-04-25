package com.example.surfaceview;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_surfaceview extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        //setContentView(R.layout.activity_main_surfaceview); 메인 액티비티

        setContentView(new GameView(this));     //GameView 출력
        ActionBar actionBar = getSupportActionBar();    // 상태바 제거
        actionBar.hide();
    }
}
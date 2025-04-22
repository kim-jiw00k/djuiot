package com.example.activitytest;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import org.w3c.dom.Text;

public class Activitytest extends AppCompatActivity {
    @Override
    protected void onStart() {
        super.onStart();
        Log.i("테스트","onStart");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.i("테스트", "onRestart");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.i("테스트", "onResume");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.i("테스트", "onPause");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i("테스트", "onDestroy");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.i("테스트", "onStop");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_activitytest);

        @SuppressLint({"MissingInflatedId", "LocalSuppress"})
        Button bt = (Button) findViewById(R.id.bt);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.google.com"));
                startActivity(intent);
            }
            // Intent 클래스는 화면 전환을 위한 클래스 이다.
        });
    }
}
package com.example.progressbar;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_progressbar extends AppCompatActivity {

    private TextView textV;
    private int progressStatus = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_progressbar);

        textV = (TextView) findViewById(R.id.tv);
        ProgressBar progressBar = (ProgressBar) findViewById(R.id.pb);
        Button btn = (Button) findViewById(R.id.bt);
        btn.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View v) {
                if(progressStatus < 100){
                    progressStatus += 10;
                    progressBar.setProgress(progressStatus);
                    textV.setText("Progress: " + progressStatus + "%");
                }
            }
        });

    }
}
package com.example.thread2;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_thread2 extends AppCompatActivity {

    private TextView text;
    private int counter = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_thread2);

        text = (TextView) findViewById(R.id.textV);
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    for(int i = 0; i < 100000; i++){
                        counter++;
                    }
                }catch (Exception e){
                    e.printStackTrace();
                }
                // 현재 스레드가 UI스레드가 아니므로 메세지 큐에 Runable을 등록한다.
                runOnUiThread(new Runnable() {
                    @SuppressLint("SetTextI18n")
                    @Override
                    public void run() {
                        // 메세지 큐에 등록될 메세지
                        text.setText(""+ counter);
                    }
                });
            }
        });
        thread.start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                try{
                    for(int i = 0; i < 100000; i++){
                        counter--;
                    }
                }catch (Exception e){
                    e.printStackTrace();
                }
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        text.setText(""+ counter);
                    }
                });
            }
        }).start();
    }
}
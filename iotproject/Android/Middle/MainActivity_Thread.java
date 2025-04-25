package com.example.thread;

import static java.lang.Thread.sleep;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_Thread extends AppCompatActivity {

    private TextView tv;
    private int counter = 0;
    private boolean isRunning = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_thread);

        tv = (TextView) findViewById(R.id.tv);

        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                while (isRunning){
                    try{
                        sleep(1000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                    counter++;
                    Log.i("테스트", "쓰레드 실행중" + counter);
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            tv.setText(String.valueOf(counter));
                        }
                    });
                }
            }
        });
        thread.start();
    }
}
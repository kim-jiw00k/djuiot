package com.example.progressbar;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_progressbar2 extends AppCompatActivity {

    private ProgressBar progressBar;
    private TextView textView;

    private Handler handler = new Handler(Looper.getMainLooper()){ // 작업스레드 --> 메인스레드로 메세지 전달
        @SuppressLint("SetTextI18n")
        // 메인스레드의 message Queue에 메세지가 쌓이고, 메인 스레드의 Looper가 하나씩 꺼내어 실행한다.
        @Override
        public void handleMessage(@NonNull Message msg) {
            super.handleMessage(msg);
            int progress = msg.what;
            progressBar.setProgress(progress);
            textView.setText("Progress : " + progress + "%");
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_progressbar2);

         progressBar = (ProgressBar) findViewById(R.id.pb2);
         textView = (TextView) findViewById(R.id.progress_text);

         new Thread(new Runnable() {
             @Override
             public void run() {
                 for(int i = 0; i <= 100; i++){
                     try{
                         Thread.sleep(100);
                     }catch (InterruptedException e){
                         e.printStackTrace();
                     }
                     handler.sendEmptyMessage(i);           // 메인의 메세지 큐에 메세지 전달
                 }
             }
         }).start();

    }
}
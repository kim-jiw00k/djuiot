package com.example.datatransfer2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity_datatransfer extends AppCompatActivity {

    private ActivityResultLauncher<Intent> launcher;
    private EditText et;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main_datatransfer);

        et = (EditText) findViewById(R.id.et);
        Button bt = (Button) findViewById(R.id.btn);
        // 런처 등록 및 콜백 함수 등록
        launcher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(),
                new ActivityResultCallback<ActivityResult>() {
                    @Override
                    public void onActivityResult(ActivityResult o) {
                        if(o.getResultCode() == RESULT_OK){
                            Intent data = o.getData();
                            if(data != null){
                                String resultData = data.getStringExtra("SubMsg");
                                et.setText(resultData);
                            }
                        }
                    }
                });
        // 버튼 클릭 시 실행 : sub 에 데이터 전달과 화면 생성하는데 launcher를 사용
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity_datatransfer.this, SubActivity_datatransfer.class);
                intent.putExtra("MainMsg", et.getText().toString());
                launcher.launch(intent);
            }
        });
    }
}
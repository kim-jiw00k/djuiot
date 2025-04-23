package com.example.datatransfer2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class SubActivity_datatransfer extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_sub_datatransfer);

        EditText et1 = (EditText) findViewById(R.id.tv);
        Button btn1 = (Button) findViewById(R.id.btn2);

        Intent intent = getIntent();
        String msg = intent.getStringExtra("MainMsg");
        et1.setText(msg);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.putExtra("SubMsg", et1.getText().toString());
                setResult(RESULT_OK, intent);
                finish();
            }
        });
    }
}
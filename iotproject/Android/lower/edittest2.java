package com.example.edittext;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {
    private TextView textView;
    private Button bt,bt2;
    private EditText ed,ed2;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main2);
        textView = (TextView) findViewById(R.id.tv);
        bt = (Button) findViewById(R.id.bt);
        ed = (EditText) findViewById(R.id.edtv);
        bt2 = (Button) findViewById(R.id.bt2);
        ed2 = (EditText) findViewById(R.id.edtv2);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = ed.getText().toString();
                ed.setText("");
                textView.setText(str);
            }
        });
        bt2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str = ed2.getText().toString();
                ed2.setText("");
                textView.setText(str);
            }
        });

    }
}
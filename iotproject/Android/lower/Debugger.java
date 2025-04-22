package com.example.debugger;

import android.os.Bundle;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class Debugger extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_debugger);

        TextView tv = (TextView) findViewById(R.id.textV);

        int result = 0;
        int a = 2, b = 3, c = 5;
        result = a << 2;
        result += b;
        result = (result + c) >> 1;
        result = add(result, b);
        tv.setText(String.valueOf(result));
    }
    int add (int aa, int bb){
        int sum = 0;
        sum = aa;
        sum += bb;
        return sum;
    }
}
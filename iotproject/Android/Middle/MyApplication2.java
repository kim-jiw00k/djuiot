package com.example.application2;

import android.app.Application;
import android.os.Bundle;
import android.util.Log;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MyApplication extends Application {

    private String id = null;
    @Override
    public void onCreate(){
        super.onCreate();
        Log.i("테스트", "어플리케이션 onCreate 함수 부름");
    }

    public void setId(String id){       // setter
        this.id = id;
    }

    public String getId(){                // getter
        return id;
    }
}
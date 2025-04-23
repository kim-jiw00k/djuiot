package com.example.application;

import android.app.Application;

public class MyApplication extends Application{
    private String globalstr;

    @Override
    public void onCreate() {
        super.onCreate();
        globalstr = "Hello MainActivity";
    }

    public String getGlobalstr() {
        return globalstr;
    }

    public void setGlobalstr(String globalstr) {
        this.globalstr = globalstr;
    }
}

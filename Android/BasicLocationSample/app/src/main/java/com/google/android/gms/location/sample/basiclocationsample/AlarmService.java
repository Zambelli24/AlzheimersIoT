package com.google.android.gms.location.sample.basiclocationsample;

import android.app.IntentService;
import android.content.ComponentName;
import android.content.Intent;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.support.v4.content.WakefulBroadcastReceiver;
import android.util.Log;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by tyler on 2/10/17.
 */

// Service for Networking and Location Updates
public class AlarmService extends IntentService {

    // Get TAG
    final static String TAG = "AlarmService";

    // Must create a default constructor
    public AlarmService() {
        // Used to name the worker thread, important only for debugging.
        super("alarm-service");

        // Do something every 5 minutes
        Timer myTimer = new Timer();
        myTimer.schedule(new TimerTask() {
            @Override
            public void run() {

            }
        }, 0, 300000);

    }

    // Constructor
    @Override
    public void onCreate() {
        super.onCreate(); // if you override onCreate(), make sure to call super().
        // If a Context object is needed, call getApplicationContext() here.

    }

    @Override
    protected void onHandleIntent(Intent intent) {
        // This describes what will happen when service is triggered
        WakefulBroadcastReceiver.completeWakefulIntent(intent);
    }

    @Override
    public ComponentName startService(Intent service) {
        return super.startService(service);
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

}
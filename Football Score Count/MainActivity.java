package com.abderahim.footballscorecounter;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

/**
 * This activity keeps track of the Football score for 2 teams.
 */
public class MainActivity extends AppCompatActivity {

    // Tracks the score for Home
    int scoreHome = 0;

    // Tracks the score for Guests
    int scoreGuest = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /**
     * Increase the score for Home by 1 point.
     */
    public void addOneForHome(View v) {
        scoreHome = scoreHome + 1;
        displayForHome(scoreHome);
    }

    /**
     * Increase the score for Home by 2 points.
     */
    public void addTwoForHome(View v) {
        scoreHome = scoreHome + 2;
        displayForHome(scoreHome);
    }

    /**
     * Increase the score for Home by 3 points.
     */
    public void addThreeForHome(View v) {
        scoreHome = scoreHome + 3;
        displayForHome(scoreHome);
    }
    /**
     * Increase the score for Home by 6 points.
     */
    public void addSixForHome(View v) {
        scoreHome = scoreHome + 6;
        displayForHome(scoreHome);
    }


    /**
     * Increase the score for Guests by 1 point.
     */
    public void addOneForGuest(View v) {
        scoreGuest = scoreGuest + 1;
        displayForGuest(scoreGuest);
    }

    /**
     * Increase the score for Guests by 2 point.
     */
    public void addTwoForGuest(View v) {
        scoreGuest = scoreGuest + 2;
        displayForGuest(scoreGuest);
    }

    /**
     * Increase the score for Guests by 3 points.
     */
    public void addThreeForGuest(View v) {
        scoreGuest = scoreGuest + 3;
        displayForGuest(scoreGuest);
    }

    /**
     * Increase the score for Guests by 6 points.
     */
    public void addSixForGuest(View v) {
        scoreGuest = scoreGuest + 6;
        displayForGuest(scoreGuest);
    }

    /**
     * Resets the score for both teams back to 0.
     */
    public void resetScore(View v) {
        scoreHome = 0;
        scoreGuest = 0;
        displayForHome(scoreHome);
        displayForGuest(scoreGuest);
    }

    /**
     * Displays the given score for Home.
     */
    public void displayForHome(int score) {
        TextView scoreView = (TextView) findViewById(R.id.home_score);
        scoreView.setText(String.valueOf(score));
    }

    /**
     * Displays the given score for Guests.
     */
    public void displayForGuest(int score) {
        TextView scoreView = (TextView) findViewById(R.id.guest_score);
        scoreView.setText(String.valueOf(score));
    }
}

package app;
import app.challenges.*;

//This file is used to run the challenge classes
public class Main {
        public static void main(String[] args) throws Exception {
            Challenge8MiniMaxSum challenge = new Challenge8MiniMaxSum();
            int[] arr = {5,4,4,5,5};
            challenge.miniMaxSum(arr);
        }

}
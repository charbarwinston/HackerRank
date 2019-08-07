package app;
import app.challenges.*;

//This file is used to run the challenge classes
public class Main {
        public static void main(String[] args) throws Exception {
            Challenge11MorganAndAString challenge = new Challenge11MorganAndAString();            
            System.out.print(challenge.morganAndString("JACK", "DANIEL"));
        }
}
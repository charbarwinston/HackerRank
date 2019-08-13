package app;

import app.challenges.*;

//This file is used to run the challenge classes
public class Main {
        public static void main(String[] args) throws Exception {
            Challenge14Kangaroo challenge = new Challenge14Kangaroo();  
            System.out.println(challenge.kangaroo(43, 2, 70, 2));
            
        }
}
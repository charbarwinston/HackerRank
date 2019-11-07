package app;

import java.util.Arrays;
import java.util.List;

import app.challenges.*;

//This file is used to run the challenge classes
public class Main {
        public static void main(String[] args) throws Exception {
            Challenge17BirthdayChocolate challenge = new Challenge17BirthdayChocolate();           

            Integer[] chocolate = {1, 2, 1, 3, 2};
            List<Integer> s = Arrays.asList(chocolate); 
            int m = 2;
            int d = 3;
            System.out.print(challenge.birthday(s, d, m));

        }
}
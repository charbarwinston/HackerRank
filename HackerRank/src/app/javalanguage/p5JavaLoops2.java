package app.javalanguage;

import java.util.Scanner;


//This file is used to run the challenge classes
public class p5JavaLoops2 {
        public static void main(String[] args) {
            int a = 0;
            int b = 2;
            int n = 10;
            int total = (int) (a + Math.pow(2, 0) * b);
            String output = total + " ";
            for (int x = 1; x < n; x++){
                total += (Math.pow(2, x) * b);
                output += total + " ";
            }
            System.out.print(output);
        }
}
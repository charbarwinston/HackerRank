package app.javalanguage;

import java.util.Scanner;


//This file is used to run the challenge classes
public class p3JavaOutputFormatting {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1 = sc.next();
                int x = sc.nextInt();
                System.out.printf("%15s %03d \n", s1, x);
            }
            System.out.println("================================");
            sc.close();
        }
}
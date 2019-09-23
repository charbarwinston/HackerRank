package app.javalanguage;

import java.util.Scanner;


//This file is used to run the challenge classes
public class p6JavaDataTypes {
        public static void main(String[] args) {
            int x = 150000;
            try
            {                
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                if(x>=Short.MIN_VALUE && x<=Short.MAX_VALUE)System.out.println("* short");
                if(x>=Integer.MIN_VALUE && x<=Integer.MAX_VALUE)System.out.println("* int");
                if(x>=Long.MIN_VALUE && x<=Long.MAX_VALUE)System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(x +" can't be fitted anywhere.");
            }
        }
}
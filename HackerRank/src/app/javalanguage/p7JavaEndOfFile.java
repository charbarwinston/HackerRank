package app.javalanguage;

import java.util.Scanner;


//This file is used to run the challenge classes
public class p7JavaEndOfFile {
        public static void main(String[] args) {
            Scanner scan = new Scanner(System.in);
            while (scan.hasNextLine()){
                System.out.println(scan.nextLine());
            }
            scan.close();
        }
}
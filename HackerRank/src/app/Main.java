package app;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import app.challenges.*;

//This file is used to run the challenge classes
public class Main {
        public static void main(String[] args) throws Exception {
            Challenge12GradingStudents challenge = new Challenge12GradingStudents();  
            int[] grades = {4,73,67,38,33}; 
            List<Integer> list = new ArrayList<Integer>();
            for (int x : grades){
                list.add(x);
            }
            challenge.gradingStudents(list);    
            
        }
}
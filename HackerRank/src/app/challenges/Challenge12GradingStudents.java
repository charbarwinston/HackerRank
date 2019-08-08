package app.challenges;

import java.util.ArrayList;
import java.util.List;

public class Challenge12GradingStudents {
    public List<Integer> gradingStudents(List<Integer> grades) {     
        ArrayList<Integer> roundedGrades = new ArrayList<Integer>();
        for (int grade: grades){
            if (grade > 35){
                int temp = grade % 10;
                if (temp < 5){
                    int normalized = Math.abs(temp - 5);
                    if (normalized < 3){
                        grade = grade + normalized;
                    }
                }
                if (temp > 5){
                    int normalized = Math.abs(temp - 10);                    
                    if (normalized < 3){
                        grade = grade + normalized;
                    }
                }
            }
            roundedGrades.add(grade);
        }        
        return (roundedGrades);
    }
}

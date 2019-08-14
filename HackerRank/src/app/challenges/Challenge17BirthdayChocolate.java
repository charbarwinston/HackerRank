package app.challenges;

import java.util.List;

public class Challenge17BirthdayChocolate {
    public int birthday(List<Integer> s, int d, int m) {
        int count = 0;
        for (int start = 0; start < s.size(); start++){
            int sum = 0;
            for (int length = 0; length < m; length++){
                try{
                    sum += s.get(start + length);
                }
                catch (Exception e){
                }

            }
            if (sum == d){
                count++;
            }
        }
        return (count);
    }
}

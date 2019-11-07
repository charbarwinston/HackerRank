package app.challenges;

import java.util.Arrays;

public class Challenge8MiniMaxSum {
    public void miniMaxSum(int[] arr) {
        //I'm proud of this one.
        long highSum = Long.MIN_VALUE;
        long lowSum = Long.MAX_VALUE;
        long[] longArray = Arrays.stream(arr).mapToLong(i -> i).toArray();
        long totalSum = Arrays.stream(longArray).sum();
        for (Long x : longArray){
            long temp = totalSum - x;
            if (temp > highSum){
                highSum = temp;
            }
            if (temp < lowSum){
                lowSum = temp;
            }            
        }
        System.out.println(highSum + " " + lowSum);

    }
}

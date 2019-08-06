package app;

import java.util.Arrays;

public class MiniMaxSum {
    public static void main(String[] args) throws Exception {
        int[] arr = {5,4,4,5,5};
        miniMaxSum(arr);
    }

    static void miniMaxSum(int[] arr) {
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

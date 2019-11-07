package app.challenges;

import java.util.List;

public class Challenge5DiagonalDifference {
    public int diagonalDifference(List<List<Integer>> arr) {
        int sum1 = 0;
        int sum2 = 0;
        for (int x = 0; x < arr.size(); x++){
            sum1 += arr.get(x).get(x);
            sum2 += arr.get(x).get(arr.size() - x - 1);
        }
        return Math.abs((sum1 - sum2));
    }
}

package app.challenges;

import java.util.Arrays;

public class Challenge4AVeryBigSum {
    public long aVeryBigSum(long[] ar) {
        return (Arrays.stream(ar).sum());
    }
}

package app.challenges;

import java.util.Arrays;

public class Challenge2SimpleArraySum {
    public int simpleArraySum(int[] ar) {
        return(Arrays.stream(ar).sum());
    }
}

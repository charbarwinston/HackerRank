package app.challenges;
public class Challenge9BirthdayCakeCandles {
    public int birthdayCakeCandles(int[] ar) {
        //This is a lot of words for a simple problem
        int tallest = Integer.MIN_VALUE;
        int count = 0;
        for (int x : ar){
            if (x > tallest){
                tallest = x;
                count = 1;
            }
            else if (x == tallest){
                count++;
            }
        }
        return count;
    }
}

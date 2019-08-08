package app.challenges;
public class Challenge13ApplesAndOranges {
    public void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {

        long hitApples = 0, hitOranges = 0;
        for (long apple: apples){
            long dropPosition = a + apple;
            if (dropPosition >= s && dropPosition <= t){
                hitApples++;
            }
        }
        for (long orange: oranges){
            long dropPosition = b + orange;
            if (dropPosition >= s && dropPosition <= t){
                hitOranges++;
            }
        }
        System.out.println(hitApples);
        System.out.println(hitOranges);
    }
}

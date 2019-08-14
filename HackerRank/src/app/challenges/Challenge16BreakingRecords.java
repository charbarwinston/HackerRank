package app.challenges;
public class Challenge16BreakingRecords {
    public int[] breakingRecords(int[] scores) {
        int max = scores[0];
        int min = scores[0];
        int maxCount = 0;
        int minCount = 0;

        for (int score: scores){
            if (score < min){
                min = score;
                minCount++;
            }
            if (score > max){
                max = score;
                maxCount++;
            }
        }
        return new int[] {maxCount, minCount};
    }
}

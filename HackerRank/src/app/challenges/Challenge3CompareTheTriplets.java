package app.challenges;

import java.util.Arrays;
import java.util.List;

public class Challenge3CompareTheTriplets {

    public List<Integer> compareTriplets(List<Integer> a, List<Integer> b){
        int as = 0;
        int bs = 0;
        for (int x = 0; x < a.size(); x++){
                if (a.get(x) > b.get(x)){
                    as++;
                }
                else if (a.get(x) < b.get(x)) {
                    bs++;
                }
            }
            return(Arrays.asList(as, bs));
    }
}

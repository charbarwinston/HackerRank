package app.challenges;

import java.util.List;

public class Challenge15BetweenTwoSets {
    public int getTotalX(List<Integer> a, List<Integer> b) {
//Brute force AF. This was stupid.
        int count = 0;
        for (int x = 1; x <= 100; x++){
            Boolean all = true;
            for (int z : a){
                    if (x % z != 0){
                        all = false;
                    }
                }
                if (all){
                    for (int y : b){
                        if (y % x != 0){
                            all = false;
                        }
                    }
                    if (all){
                        count++;
                    }
                }
            }
        return(count);
    }

}


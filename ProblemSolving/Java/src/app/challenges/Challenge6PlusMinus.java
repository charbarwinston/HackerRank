package app.challenges;

import java.text.DecimalFormat;
import java.text.NumberFormat;
public class Challenge6PlusMinus {
    //Shh it works.
        public void plusMinus(int[] arr) {
            float positive = 0;
            float negative = 0;
            float zero = 0;
            NumberFormat formatter = new DecimalFormat("#0.00000");
            for (int x = 0; x < arr.length; x++){
                if (arr[x] > 0){
                    positive++;
                }
                else if (arr[x] < 0){
                    negative++;
                }
                else{
                    zero++;
                }
            }
        System.out.println(formatter.format(positive / arr.length) + "\n" + formatter.format(negative / arr.length) + "\n" + formatter.format(zero / arr.length)); 
    }
}

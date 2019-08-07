package app.challenges;

public class Challenge11MorganAndAString {
    public String morganAndString(String a, String b) {
        String result = "";
        while (a.length() >= 1 && b.length() >= 1){
            if (a.charAt(0) > b.charAt(0)){
                result = result + b.charAt(0);
                if (b.length() != 0){
                    b = b.substring(1);
                }
            }
            else if (a.charAt(0) < b.charAt(0)){
                result = result + a.charAt(0);
                if (a.length() != 0){
                    a = a.substring(1);
                }
            }
            else {
                result = result + a.charAt(0);
                if (a.length() != 1){
                    a = a.substring(1);
                }
                else {
                    b = b.substring(1);
                }
            }
        }
        return result + a + b;
    }
}

package app.challenges;
public class Challenge14Kangaroo {
    public String kangaroo(int x1, int v1, int x2, int v2) {
        if (x1 > x2 && v1 > v2){
            return "NO";
        }
        else if (x2 > x1 && v2 > v1){
            return "NO";
        }
        
        
        return "";
    }

}

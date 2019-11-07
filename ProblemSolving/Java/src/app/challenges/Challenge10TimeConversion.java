package app.challenges;
public class Challenge10TimeConversion {
    //Brute force!!!
    public String timeConversion(String s) {
        String[] split = s.split(":");    
        if (s.contains("PM")){
            if (split[0].equals("12")){
                split[0] = "12";
            }
            else{
                split[0] = Integer.toString((Integer.parseInt(split[0]) + 12));                
            }
            split[2] = split[2].replace("PM", "");
        }
        else if (s.contains("AM")){            
            if (split[0].equals("12")){
                split[0] = "00";
            }
            split[2] = split[2].replace("AM", "");
        }
        System.out.println(split[0]);
        return (split[0] + ":" + split[1] + ":" + split[2]);
    }
}

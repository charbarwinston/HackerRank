package app.challenges;

public class Challenge7Sstairs {
    public void staircase(int n) {
        //This took... a long time...
        for (int x = 0; x < n; x++)
        {
            String s = new String(new char[x + 1]).replace("\0", "#");
            System.out.println(String.format("%1$" + (n - x) + "s", s));
        }

    }
}

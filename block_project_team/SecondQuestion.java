package block_project_team;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class SecondQuestion {
    public static void main(String[] args) throws IOException {
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));

        String score = buffer.readLine();

        if (score.equals("100")){
            System.out.println("A");
            return;
        }else if(score.length() == 1){
            System.out.println("F");
            return;
        }
        char tenth_digit = score.charAt(0);
        switch(tenth_digit){
            case '9':
                System.out.println("A");
                break;
            case '8':
                System.out.println("B");
                break;
            case '7':
                System.out.println("C");
                break;
            case '6':
                System.out.println("D");
                break;
            default:
                System.out.println("F");
                break;
        }

    }
}

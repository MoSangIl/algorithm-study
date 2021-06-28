package block_project_team;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class FirstQuestion{
    public static void main(String args[]) throws IOException{
        Scanner scanner = new Scanner(System.in);

        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();

        if (a > b){
            System.out.println(">");
        }else if(a < b){
            System.out.println("<");
        }else{
            System.out.println("==");
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		int a1 = Integer.parseInt(st.nextToken());
		int b1 = Integer.parseInt(st.nextToken());
		
		System.out.println((a1>b1) ? (">") : ((a1<b1) ? ("<") : ("==")));
    }
}
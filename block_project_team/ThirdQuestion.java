package block_project_team;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class ThirdQuestion {

    public static void main(String[] args) throws IOException {
        
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
    
    
        int num = buffer.read() - 48;
    
        for (int i = 1; i < 10; i++){
            System.out.printf("%d * %d = %d\n", num, i, num*i);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        
        for(int i = 1; i <= 9; i++) {
            sb.append(n).append(" * ").append(i).append(" = ").append(n*i).append("\n");
        }
        System.out.print(sb);
    }
}

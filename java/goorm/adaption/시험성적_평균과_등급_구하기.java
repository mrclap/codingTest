import java.io.*;

class Main {
	public static void main(String[] agrs) throws Exception {
		String input = "100 100 98";
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		String input = br.readLine();

		String[] scoreList = input.split(" ");
		float avg = 0;
		char grade = ' ';
		for (String score:scoreList){
			avg += Float.valueOf(score);
		}
		avg = avg / scoreList.length;
		if (avg >= 90) {
			grade = 'A';
		}else if(avg >= 80) {
			grade = 'B';
		}else if(avg >= 70) {
			grade = 'C';
		}else if(avg >= 60) {
			grade = 'D';
		}else {
			grade = 'F';
		}

		System.out.printf("%.2f %c", avg, grade);
	}
}
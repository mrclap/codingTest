import java.io.*;
import java.math.BigInteger;

class Main {
	public static void main(String[] agrs) throws Exception {
		int[] favoriteNumberList = {2,3,6};
		final int favoriteNumCount = favoriteNumberList.length;
		String input = "30";
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		String input = br.readLine()
		BigInteger answer = recursive(BigInteger.ONE, BigInteger.ZERO, favoriteNumCount, Integer.parseInt(input));
		System.out.println(answer);
		return;
	}

	public static BigInteger recursive(BigInteger previous, BigInteger sum, int num, int count) {
		if (count > 0) {
			previous = previous.multiply(BigInteger.valueOf((long)num));
			sum = sum.add(previous);
			count -= 1;
			return recursive(previous, sum, num, count);
		}	else {
			return sum;
		}
	}
}
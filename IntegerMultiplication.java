
public class IntegerMultiplication {

	public IntegerMultiplication() {
		// TODO Auto-generated constructor stub
	}

	public int[] multiply(int num1[], int num2[])
	{
		int result[] = new int[num1.length + num2.length];
		int temp = 0;
		int carry  = 0;
		for (int m = num1.length -1 ; m >= 0 ; m--){
			carry = 0;
			temp = 0;
			for (int n = num2.length -1 ; n >= 0 ; n--){
				temp = num1[m] * num2[n] + carry + result[m+n];
				result[m+n] = temp % 10 ;
				carry = (temp/10);
			}
		}
		
		for (int i = 0 ; i < result.length ; i++)
		{
			System.out.println(result[i]);
			
		}
		return result;
	}
	public static void main(String[] args) {
		
		int num1[] = {2,3,5};
		int num2[] = {1,3,1,1,2,9};
		int result[];
		IntegerMultiplication im = new IntegerMultiplication();
		result = im.multiply(num1,num2);
		
	}

}

/**
 * 
 */




public class LargestSumSequence {

	private int length;
	public LargestSumSequence(int arr[]) {
		System.out.println("Constructor Bitch");
		length = arr.length;
 		// TODO Auto-generated constructor stub
	}
	
	public int getMax(int sum[])
	{
		int max = Integer.MIN_VALUE;
		
		for(int i = 0  ; i < sum.length ; i++)
		{
			if(sum[i] > max)
			{
				max = sum[i];
			}		
			
		}
			
		return max;
	}
	
	public int getLargestSumSequence(int arr[]) {
	
		
		int sum[] = new int[this.length];
		sum[0] = arr[0];
		for(int i = 1; i < this.length ; i++)
		{
			sum[i] = Math.max(arr[i], (sum[i-1] + arr[i]));
			
		}
	
	return getMax(sum);
	}
	
	
	public static void main(String[] args) {
		
		int arr[] = {-6,12,-7,0,14,7,15};
		LargestSumSequence LSS = new LargestSumSequence(arr);
		
		int value = LSS.getLargestSumSequence(arr);
		System.out.println("Maximum Subsequence is " + value);
	
	}

}

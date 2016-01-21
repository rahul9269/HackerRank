
public class LongestPlaindrome {

	public StringBuilder str1;
	public StringBuilder str2;
	public LongestPlaindrome(StringBuilder s1) {
		
		this.str1 = new StringBuilder(s1);
		this.str2 = new StringBuilder(s1);
		str2.reverse();
		// TODO Auto-generated constructor stub
	}

	public  int longestP()
	{
		
		System.out.println(str1);
		System.out.println(str2);
		int length = 0;
		int[][] dp = new int[str1.length() + 1][str2.length() + 1];
		
		for (int i = 1; i <= str1.length();i++)
		{
			for (int j = 1 ; j <=str2.length();j++)
			{
				if (str1.charAt(i-1) == str2.charAt(j-1))
				{	
					dp[i][j] = dp[i-1][j-1] + 1;
					if(length < dp[i][j])
					{
						length = dp[i][j];
						
					}
				}
			
			}
			
		}
		
		System.out.println(length);
		for(int i = 0; i<=str1.length(); i++)
		{
		    for(int j = 0; j<=str2.length(); j++)
		    {
		        System.out.print(dp[i][j]);
		    }
		    System.out.println();
		}
		
		return length;
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	String s = "caba";
	StringBuilder s1 = new StringBuilder(s);

	LongestPlaindrome lp = new LongestPlaindrome(s1);

	int lenght = lp.longestP();
	
	}

}

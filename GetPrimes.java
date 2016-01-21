

import java.util.ArrayList;
import java.util.Scanner;
public class GetPrimes {

	
	public boolean primes[]; 
	
	public GetPrimes(int n) {
		
		primes = new boolean[n];
		
		
		for(int i = 2 ; i < n ; i++)
		{
			
			this.primes[i] = true;
			
		}
		
		this.primes[0] = this.primes[1] = false;
		
		
	}

	public boolean isPrime(int n)
	{
		if (n == 2)
			return true;
		if (n%2 == 0)
			return false;
		
		for (int i = 3 ; i * i < n ; i+=2)
		{
			if(n%i==0)
				return false;
			
		}
	
		
		return true;
	}
	
	public boolean[] getPrimes()
	{
		for (int i = 2; i < this.primes.length ; i++)
		{
			if(this.primes[i])
			{
				if(this.isPrime(i))
				{
					for(int j = i; j<this.primes.length; j+=i)
					{
						this.primes[j] = false;
						
					}
					this.primes[i] = true;	
				}
				
			}
			
		}
		
		
		return this.primes;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean list[];
		Scanner user_input = new Scanner( System.in );
		System.out.println("Please Enter the number");
		int n = Integer.parseInt(user_input.next());
		System.out.println(n);
		GetPrimes rp = new GetPrimes(n);
		list = rp.getPrimes();
		for (int i = 0; i < n ; i ++)
		{	
			if(list[i])
			{
				System.out.print(i+",");
			}
			
			
		}
	
	}

}

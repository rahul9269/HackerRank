public class DeleteDuplicateEntries {

	int carr[];
	public DeleteDuplicateEntries(int arr[]) {
		// TODO Auto-generated constructor stub

		this.carr = arr;
	}
  

	public  void removeDuplicates()
	{
		
		int j = 1;
		for (int i = 1 ; i < this.carr.length;  i++)
		{
			
			if (this.carr[j-1] != this.carr[i])
			{
				this.carr[j] = this.carr[i];
				j++;
				System.out.println("ad");
				
			}
			
		}
		
		for(int i = 0 ; i < this.carr.length ; i ++)
		{
			System.out.println(this.carr[i]);
			
		}
		
	}
	
	public static void main(String[] args) {
		
	int arr[] = {1,1,4,5,6};
	DeleteDuplicateEntries dq = new DeleteDuplicateEntries(arr);	
	dq.removeDuplicates();
	
	
	
	}

}

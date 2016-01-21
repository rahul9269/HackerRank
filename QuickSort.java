
public class QuickSort {

	int carr[];
	public QuickSort(int arr[]){
		this.carr = arr;
		
	
	}

//	public int partition(int arr[], int low, int high){
	public int partition(int low, int high){
		int pivot = this.carr[high];
		int i = low;
		int temp;
		for (int l = low ; l < high ; l++)
		{
			if (this.carr[l] <=  pivot)
			{
				temp = this.carr[i];
				this.carr[i] = this.carr[l];
				this.carr[l] = temp;
				i++;
			}
			
		}
		this.carr[high] = this.carr[i];
		this.carr[i] = pivot;	

		return i;
	}
	
//	public void QuickSortmethod(int arr[],int low, int high)
	public void QuickSortmethod(int low, int high)
	{
		int p;
		if (low < high)
		{
			p = partition(low, high);
			QuickSortmethod(low, p-1);
			QuickSortmethod(p+1,high);
//			
		}	
		

	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int arr[] = {-6,12,-7,0,14,7,15};
	QuickSort qs = new QuickSort(arr);
	qs.QuickSortmethod(0, arr.length - 1);
	

	for (int j = 0 ; j < qs.carr.length ; j ++)
	{
	System.out.println("Array " + qs.carr[j]);
	}
	
	}

}

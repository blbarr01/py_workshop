#include <stdio.h> 
#include <stdlib.h>
#include <time.h> 

void print_arr(int *arr, int n)
{
	for(int i = 0; i < n; i++)
		printf("%d ", arr[i]);

printf("\n");

}

void insert_sort(int *arr,int n)
{
	int temp;
	for(int i =0; i<n; i++)
	{
		for(int j =0; j<n; j++)
		{
			if(arr[j] > arr[i])
			{
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;	
			}	
		}
	}
}

void merge_sort(int *arr, int n)
{	
	if(n <= 1) return; 
	
	int mid = n / 2;
	// create arrays of appropriate sizes
	int left[mid], right[n-mid];
	for(int i = 0; i < mid; i++){
		left[i] = arr[i];
	}
		
	for(int i = mid; mid< n; i++)
	{
		right[i-mid] = arr[i];
	}

	merge_sort(left, sizeof left / sizeof left[0]);
	merge_sort(right, sizeof right / sizeof right[0]);

}
int main(int argc, char *argv[])
{
	// parse input 
	int n;
	if(argv[1])
		n = atoi(argv[1]);
	else
		 n = 10;

	// generate random sequence 
	int arr[n];
	printf("%d\n", 5/2);
	printf("%d\n", n/2);
	srand(time(NULL));
	for(int i = 0; i < n; i++)
		arr[i] = rand()%100;
	
	print_arr(arr, n);	
	insert_sort(arr, n);
	print_arr(arr, n);	
	
	return 0;
}	

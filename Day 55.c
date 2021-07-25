#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int C[5];

int *merge(int *A, int m, int *B, int n) 
{
	int i=0, j=0, k=0;
	while(i<=m && j<=n)
		if (A[i] < B[i])
			C[k++] = A[i++];
		else
			C[k++] = B[j++];;
	
	while (i<=m)
		C[k++] = B[j++];
		
	while (j<=n)
		C[k++] = B[j++];
		
	return C;
}

int *mergesort(int *A, int l, int r) 
{

	if (l>=r)
		return &A[l];
	int m = (l+r)/2;
	return merge(mergesort(A,l,m), m-l+1, mergesort(A,m+1,r), r-m);
}

int main()
{
	int a[5]={2,9,4,6,3}, s=5;
	int *n;
	n = mergesort(a,0,s-1);
	printf("Sorted Array: ");
	for(int i=0; i<s; i++)
		printf("%d ", n[i]);
	printf("\n");
	return 0;
}

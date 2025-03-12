#include <stdio.h>

void showarrayelem(int*,int);

int main()
{
	int arr1[3] = {1 ,2 ,3};
	int arr2[5] = {4 ,5 ,6 ,7 ,8};
	showarrayelem(arr1, sizeof(arr1) / sizeof(int));
	showarrayelem(arr2, sizeof(arr2) / sizeof(int));
	return 0;
}

void showarrayelem(int param[], int len)
{
	int i = 0;
	for(i; i < len; ++i)
	{
		printf("%d ", param[i]);
	}
	printf("\n");
}

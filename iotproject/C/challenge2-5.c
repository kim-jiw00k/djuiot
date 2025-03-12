#include <stdio.h>

void dessort(int *, int);

int main()
{
	int i = 0;
	int arr[7] = {};
	for(i = 0; i < 7;  ++i)
	{
		printf("정수 입력 : ");
		scanf("%d", &arr[i]);
	}
	dessort(arr , sizeof(arr) / sizeof(int));
	for(i = 0; i < 7; ++i)
	{
		printf("%d ", arr[i]);
	}


	return  0;
}

void dessort(int* num , int len)
{
	int i = 0;
	int j = 0;
	int temp = 0;

	for(i = 0; i < len; ++i)
	{
		for(j = 0; j < len; ++j)
		{
			if(num[j] > num[j-1])
			{
				temp = num[j-1];
				num[j-1] = num[j];
				num[j] = temp;
			}
		}
	}
}

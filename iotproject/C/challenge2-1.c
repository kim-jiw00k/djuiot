#include <stdio.h>

void hol(int*, int);
void jjak(int*, int);


int main()
{
	int i = 0;
	int arr[10] = {};
	
	for(i=0; i<10; ++i)
	{
		printf("정수 입력 : ");
		scanf("%d", &arr[i]);
	}
	hol(arr, sizeof(arr) / sizeof(int));
	jjak(arr, sizeof(arr)/ sizeof(int));
	return 0;
}

void hol(int* holl, int len)
{
	int i;
	//len = 10;
	printf("홀수 출력 : ");
	for(i = 0 ; i < len; ++i)
	{
		if(holl[i] % 2 != 0)
		{
			printf("%d ", holl[i]);
		}
	}
	printf("\n");
}

void jjak(int* jjak, int len)
{
	int j;
	//len = 10;
	printf("짝수 출력 : ");
	for(j = 0; j < len; ++j)
	{
		if(jjak[j] % 2 == 0)
		{
			printf("%d ", jjak[j]);
		}
	}
	printf("\n");
}

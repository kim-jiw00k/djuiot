#include <stdio.h>

int main()
{
	int num = 1;	// 입력 받을 수
	int p = 0;		// 양수
	int n = 0;		// 음수
	int z = 0;		// 0
	int count = 0;	// 총 카운팅 수

	printf("몇 번 입력을 받을건지? : ");
	scanf("%d",&num);
	for(int j = 0;j < num;++j)
	{
		int i = 0;
		printf("정수 입력 : ");
		scanf("%d", &i);

		if(i < 0)
		{
			++n;
		}
		else if(i > 0)
		{
			++p;
		}
		else
		{
			++z;
		}
	}
	count = p+n+z;
	printf("양수는 %d번 음수는 %d번 0은 %d번해서 총 %d번 카운트 \n", p, n, z, count);
	return 0;
}

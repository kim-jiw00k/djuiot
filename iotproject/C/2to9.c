#include <stdio.h>

int main()
{
	int cur = 2;
	int is = 0;
	int n = 0;

	printf("몇 단 까지 출력 할까요? : ");
	scanf("%d", &n);

	for(;cur <= n;++cur)					//while(cur <= n)-> for문 조건식으로 들어감 
											//2 단 부터 n 단까지 반복
	{
		printf("%d단 \n", cur);				//몇 단인지 알려주는 출력 코드.
											//is = 1; 이것이 for문 초기식으로 들어감
		for(is = 1;is < 10;++is)			//while(is<10)-> for문 조건식으로 들어감
											//각 단의 1부터 9의 곱을 표현
		{
			printf("%d X %d = %d \n", cur, is ,cur*is);
											//is = is + 1; -> ++is
		}
											//cur = cur+1; -> ++cur
	}

	return 0;
	/*주석은 while중첩문 바꾼거는 for 중첩문*/
}

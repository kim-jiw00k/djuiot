#include <stdio.h>

int main()
{
	int villa[4][2];
	int popu = 0;
	int i = 0;
	int j = 0;

	/*가구별 거주인원 입력 받기*/
	for(i = 0; i < 4; ++i)	//층
	{
		for(j = 0; j < 2; ++j)	// 호수
		{
			printf("%d층 %d호 인구수 : ", i+1, j+1);
			scanf("%d", &villa[i][j]);
		}
	}
	/*빌라의 층별 인구수 출력하기*/
	for(i = 0; i < 4; ++i)
	{
		popu = 0;
		popu += villa[i][0];
		popu += villa[i][1];
		printf("%d층 인구수 : %d \n", i+1, popu);
	}
	return 0;
}

#include <stdio.h>
#include <string.h>

int main()
{
	char str1[20] = {'\0'};
	char str2[20] = {'\0'};
	printf("문자열 입력 : ");
	fgets(str1,sizeof(str1),stdin);
	printf("문자열 입력 : ");
	fgets(str2,sizeof(str2),stdin);

	if(! strcmp(str1, str2))
	{
		puts("두 문자열은 완벽히 동일합니다.");
	}
	else
	{
		puts("두 문자열은 동일하지 않습니다.");

		if(!strncmp(str1, str2, 3))
		{
			puts("그러나 앞 세글자는 동일합니다.");
		}
	}
}

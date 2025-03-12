#include <stdio.h>
#include <string.h>

int main(int argc, const char* argv[])
{

	char str[1024] = {'\0',};
	puts("문자열 입력");
	scanf("%s", str);
	printf("입력된 문자열의 길이 : %lu\r\n", strlen(str));
	unsigned long str_length = strlen(str);
	
	for(int i = 0u; i < (int)str_length / 2; ++i)
	{
		if(str[i] != str[str_length - i - 1])
		{
			printf("회문이 아닙니다. \n");
			break;
		}
	}
	return 0;
}

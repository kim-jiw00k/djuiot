#include <stdio.h>
#include <stdlib.h>
int main()
{
	puts("Hello World"); // \n 기본적으로 개행문자가 자동으로 개입
	const char* str = "Welcome my home \n";
	fputs(str, stdout);
	
	char buffer[BUFSIZ] = {'\0',}; // BUFFSIZ 512
	fputs("문자열 입력 : ", stdout);
	fgets(buffer, BUFSIZ, stdin); // buffer overflow 방지
	puts(buffer); // 문자열 출력
	fprintf(stdout,"%s\n", buffer);

	return 0;
}

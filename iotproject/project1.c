#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

void lgin(); //로그인 동의 함수
void login(); // 로그인 화면 함수

struct Loginfo
{
	char id[20];
	char passwd[20];
};

int main()
{
	lgin();		//로그인 동의
	login();	//로그인 화면

	return 0;
}

void lgin()		//시작 시 로그인 동의
{
	int access = 0;
	while(1)		//아니오를 고를경우 무한 되물음
	{
		printf("로그인을 할 것인가요?\n 예 : 1\t 아니오 : 2 \n");
		scanf("%d", &access);	
		if(access == 1)
		{
			system("clear");	//화면 초기화
			printf("로그인 화면으로 이동 합니다.\n");
			sleep(3);			//3초후 초기화 에서 3초후
			system("clear");	// 초기화
			break;				//1 고를 경우 무한루프 탈출
		}
		else if(access == 2)
		{
			system("clear");
			printf("로그인을 하지 않습니다.\n");
			sleep(3);
			system("clear");
		}
	}
}
//로그인 화면 함수
void login()
{
	struct Loginfo user1 = {'\0', '\0'};
	struct Loginfo user2 = {'\0', '\0'};
	strcpy(user1.passwd, "1234");
	while(1)
	{
		printf("ID : ");
		scanf("%s",user1.id);	
		printf("PASSWD (기본 1234) : ");
		scanf("%s",user2.passwd);
		if(strcmp(user1.passwd, user2.passwd))
		{
			printf("비밀번호가 다릅니다.\n");
		}
		else
		{
			printf("로그인 되었습니다.\n");
			break;  //비밀 번호가 맞을 시 탈출
		}
		sleep(1);
		system("clear");
	}
}

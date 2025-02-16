#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

void lgin(); //로그인 동의 함수
void login(); // 로그인 화면 함수
void accetime(); // 본인 확인 및 시간
void screen();	//초기 화면
void productin(); //제품 입력

struct Loginfo
{
	char id[20];
	char passwd[20];
};
struct Product
{
	char prodname[20];	//이름
	char makename[20];	//제조사
	char exp[20];		//유통기한
	char adult[20];		//성인여부
	int price;			//가격
	int stack;			//재고
}
// 전역 변수로 하여 다른 함수들에서도 쓸 수 있게 만듬
struct Loginfo user1 = {'\0', '\0'};
struct Loginfo user2 = {'\0', '\0'};
struct Product prod1[20];

int main()
{
	lgin();		//로그인 동의
	login();	//로그인 화면
	accetime(); //본인 확인 및 시간
	time_t start = time(NULL);	//시작 시간
	screen();		//초기 화면
	

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
	}
}

void accetime()
{
	system("clear");
	int acc = 0;	//확인
	printf("사원 %s 본인이 맞습니까? : ", user1.id);
	scanf("%d", &acc);
	while(1)
	{
		if (acc == 1)
		{
			printf("확인 되었습니다.\n");
			sleep(1);
			system("clear");
			printf("현재 잔고 : 1,234,000 원 \n");
			sleep(1);
			system("clear");
			break;
		}
		else(acc == 2);
		{
			printf("다시 로그인 합니다.\n");
			login();
			accetime();
			break;
		}
	}
}

void screen();
{
	int num;	// 어디갈지 입력 받음
	printf("1. 제품 입력\t2. 제품확인\n");
	scanf("%d", &num);
	if(num == 1)
	{
		printf("제품 입력으로 이동합니다.");
		sleep(1);
		system("clear");
		productin();
	}
	else(num == 2)
	{
		printf("제품 확인으로 이동합니다.");
	}
}
// 해결해야할 문제
void productin();
{
	printf("1. 제품명 입력 : ");
	scnaf("%s", prod[i].prodname);
	printf("2. 제조회사 입력 : ");
	scanf("%s", prod[i].makename);
	printf("3. 유통기한 입력 :");
	scanf("%s", prod[i].exp);
	printf("4. 19금 물건 확인(1 : 예 , 0 : 아니오) : ");
	scanf("%s", prod[i].adult);
	printf("5. 가격");
	scanf("%s", prod[i].price);
	prod[i]
}

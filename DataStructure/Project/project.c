#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct Car
{
	char num[10];
	struct Car* link;
}car;

car * head = NULL;	//링크드 리스트의 헤드 포인터

void screen();	//초기 화면
void add_screen();		//추가 화면
void print_screen();	//조회 화면
//void find_screen();		//찾기 화면
int add(car ** carnum, char * str);	//추가 하는 함수


int main()
{
	screen();

	return 0;
}
void screen()
{
	int choice = 0;
	printf("\t\t***** 주차 관리 시스템 *****\n");
	printf("번호를 입력하시면 이동합니다.\n1. 차량 추가  2. 차량 조회  3. 차량 검색\n");
	printf("번호 입력 : ");
	scanf("%d", &choice);
	if(choice == 1)
	{
		printf("차량 추가로 이동합니다.\n");
		sleep(1);
		system("clear");
		add_screen();
	}
	else if(choice == 2)
	{
		printf("차량 조회로 이동합니다.\n");
		sleep(1);
		system("clear");
		print_screen();
	}
	else if(choice == 3)
	{
		printf("차량 검색으로 이동합니다.\n");
		sleep(1);
		system("clear");
		//find_screen();
	}
	else
	{
		printf("잘못 된 선택입니다.\n");
		screen();
	}
}

int add(car ** carnum, char * str)
{
	car * node = (car*)malloc(sizeof(car));
	strcpy(node -> num,str);
	if(*carnum == NULL)
	{
		*carnum = node;
		node -> link = NULL;
	}
	else
	{
		car * current = *carnum;
		while(current -> link != NULL)
		{
			current = current -> link;
		}
		current -> link = node;
		node -> link = NULL;
	}
	return 0;
}

void add_screen()		//추가 화면 함수
{
	char carn[100];
	car * head = NULL;
	printf("***** 차량 번호 추가 *****\n");
	printf("추가할 차량 번호를 입력하시오. : ");
	scanf("%s", &carn);
	add(&head, carn);		//head에다가 carn을 추가 한다.
	printf("추가 완료! \n");
	sleep(1);
	system("clear");
	screen();
}
/*
void print_screen()		//조회 화면 함수
{
	int ex = 0;
	printf("***** 차량 번호 조회 *****\n(0 이외에 숫자 입력 후 엔터 시 종료)\n");
	car * current = head;
	while(current != NULL)
	{
		printf("%s\n",current -> num);
		current = current -> link;
	}
	scanf("%d", &ex);
	if(ex != 0)
	{
		system("clear");
		index_win();
	}
}*/

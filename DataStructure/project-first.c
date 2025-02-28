#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct Car
{
	char num[10];
	struct Car* link;
}car;

void index_screen();	//초기 화면
void add_screen();		//추가 화면
void print_screen();	//조회 화면
void find_screen();		//찾기 화면
//int add(car ** carnum, char * str);	//추가 하는 함수


int main()
{
	index_screen();

	return 0;
}
void index_screen()
{
	int choice = 0;
	printf("\t\t***** 주차 관리 시스템 *****\n");
	printf("번호를 입력하시면 이동합니다.\n1. 차량 추가  2. 차량 조회  3. 차량 검색\n");
	printf("번호 입력 : ");
	scanf("%d", &choice);
	while(1)
	{
		if(choice == 1)
		{
			printf("차량 추가로 이동합니다.\n");
			sleep(1);
			system("clear");
			break;
			add_screen();
		}
		else if(choice == 2)
		{
			printf("차량 조회로 이동합니다.\n");
			sleep(1);
			system("clear");
			break;
			print_screen();
		}
		else if(choice == 3)
		{
			printf("차량 검색으로 이동합니다.\n");
			sleep(1);
			system("clear");
			break;
			find_screen();
		}
		else
		{
			printf("잘못 된 선택입니다.\n");
			index_screen();
		}
	}

}

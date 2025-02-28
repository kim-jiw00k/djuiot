#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct Car
{
	char num[10];
	struct Car* link;
}car;

typedef struct
{
	car * head;
}carhead;

car * head = NULL;	//링크드 리스트의 헤드 포인터

void screen();			//초기 화면
void add_screen();		//추가 화면
void print_screen();	//조회 화면
void delete_screen();	//삭제 화면
void clear();			//종료 화면
int add(car ** carnum, char * str);	//추가 하는 함수
int delete(car ** carnum, int index);//삭제 하는 함수
//car * search(car* head, char* x);	//찾는 함수
void print();						//조회 하는 함수



int main()
{
	screen();
	clear(&head);

	return 0;
}
void screen()
{
	int choice = 0;
	printf("\t\t***** 주차 관리 시스템 *****\n");
	printf("번호를 입력하시면 이동합니다.\n1. 차량 추가  2. 차량 조회  3. 차량 삭제 4. 종료\n");
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
		printf("차량 삭제로 이동합니다. \n");
		sleep(1);
		system("clear");
		delete_screen();
	}
	else if(choice == 4)
	{
		printf("종료 합니다.\n");
		sleep(1);
		system("clear");
		return;
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
	printf("\t\t***** 차량 번호 추가 *****\n");
	printf("추가할 차량 번호를 입력하시오. : ");
	scanf("%s", carn);
	add(&head, carn);		//head에다가 carn을 추가 한다.
	printf("추가 완료! \n");
	sleep(1);
	system("clear");
	screen();
}

void print_screen()		//조회 화면 함수
{
	int ex = 0;
	printf("\t\t***** 차량 번호 조회 *****\n(0 이외에 숫자 입력 후 엔터 시 종료)\n");/*
	car * current = head;
	while(current != NULL)
	{
		printf("%s\n",current -> num);
		current = current -> link;
	}*/print();
	scanf("%d", &ex);
	if(ex != 0)
	{
		system("clear");
		screen();
	}
}

void clear()
{
	car * current = head;
	while(current != NULL)
	{
		car * link = current -> link;
		free(current);
		current = link;
	}
	head = NULL;
}

int delete(car ** carnum, int index)
{
	if(head == NULL)
	{
		return -1;
	}
	else if(index == 0)
	{
		car * node = head;
		head = node -> link;
		free(node);
	}
	else
	{
		car * current = head;
		car * prev = NULL;
		for(int i = 0; i < index; ++i)
		{
			if(current == NULL)
			{
				return -1;
			}
			prev = current;
			current = current -> link;
		}
		prev -> link = current -> link;
		free(current);
	}
	return 0;
}

void delete_screen()
{
	int carn = 0;
	int i = 1;
	printf("\t\t***** 차량 번호 삭제 *****\n");
	car * current = head;
	while(current != NULL)
	{
		printf("%d.%s\n", i, current -> num);
		current = current -> link;
		++i;
	}
	printf("삭제 할 차량의 번호를 입력 하시오. : ");
	scanf("%ls", &carn);
	delete(&head,carn);
	printf("삭제 완료 !\n");
	sleep(1);
	system("clear");
	screen();
} 

/*car * search(car* head,char* x)
{
	car* temp;	
	while(temp != NULL)
	{
		if(strcmp(temp -> num,x, strlen(x)) == 0) return temp;
		else temp = temp -> link;
	}
	return NULL;
}*/

void print()
{
	car * current = head;
	while(current != NULL)
	{
		printf("%s\n",current -> num);
		current = current -> link;
	}
}

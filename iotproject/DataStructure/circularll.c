#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct ListNode
{
	char data[4];
	struct ListNode * link;
}listNode;

typedef struct
{
	listNode * head;
}linkedList;

linkedList * createLList_h(void);
void print(linkedList* CL);
void instnode(linkedList* CL, char* x);
void insmidnode(linkedList* CL, listNode* pre,char * x);
void delete(linkedList* CL, listNode* old);
listNode *search(linkedList* CL, char* x);

int main()
{
	linkedList *CL;
	listNode *p;

	CL = createLList_h();
	printf("(1) 원형 연결 리스트 생성하기 !\n");
	print(CL);

	printf("\n(2) 원형 연결 리스트에 [월] 노드 삽입하기 !\n");
	instnode(CL,"월");
	print(CL);

	printf("\n(3) 원형 연결 리스트의 [월] 노드 뒤에 [수] 노드 삽입하기 !\n");
	p = search(CL,"월"); insmidnode(CL, p, "수");
	print(CL);

	printf("\n(4) 원형 연결 리스트의 [수]노드 뒤에 [금] 노드 삽입하기 !\n");
	p = search(CL ,"수"); insmidnode(CL, p, "금");
	print(CL);

	printf("\n(5) 원형 연결 리스트에서 [수] 노드 삭제하기 !\n");
	p = search(CL,"수"); delete(CL,p);
	print(CL);

	getchar();return 0;
}

linkedList * createLList_h(void)
{
	linkedList* CL;
	CL = (linkedList*)malloc(sizeof(linkedList));
	CL -> head = NULL;
	return CL;
}
void print(linkedList* CL)
{
	listNode* p;
	printf(" CL = (");
	p = CL -> head;
	if(p == NULL)
	{
		printf(")\n"); return;
	}
	do
	{
		printf("%s",p -> data);
		p = p -> link;
		if(p != CL -> head) printf(", ");
	}while(p != CL -> head);
	printf(") \n");
}
void instnode(linkedList* CL, char* x)
{
	listNode* newNode, *temp;
	newNode = (listNode*)malloc(sizeof(listNode));
	strcpy(newNode -> data, x);
	if(CL -> head == NULL)
	{
		CL -> head = newNode;
		newNode -> link = newNode;
	}
	else
	{
		temp = CL -> head;
		while(temp -> link != CL -> head)
		{
			temp = temp -> link;
		}
		newNode -> link = temp -> link;
		CL -> head = newNode;
	}
}
void insmidnode(linkedList* CL, listNode* pre,char * x)
{
	listNode* newNode;
	newNode = (listNode*)malloc(sizeof(listNode));
	strcpy(newNode -> data, x);
	if(CL -> head == NULL)
	{
		CL -> head = newNode;
		newNode -> link = newNode;
	}
	else
	{
		newNode -> link = pre -> link;
		pre -> link = newNode;
	}
}
void delete(linkedList* CL, listNode* old)
{
	listNode *pre;
	if(CL -> head == NULL)return;
	if(CL -> head -> link == CL -> head)
	{
		free(CL -> head);
		CL -> head = NULL;
		return;
	}

	else if(old == NULL) return;
	else
	{
		pre = CL -> head;
		while (pre -> link != old)
		{
			pre = pre -> link;
		}
		pre -> link = old -> link;
		if(old == CL -> head)
		{
			CL -> head = old -> link;
		}
		free(old);
	}
}

listNode *search(linkedList* CL, char* x)
{
	listNode *temp;
	temp = CL -> head;
	if(temp == NULL)return NULL;
	do
	{
		if(strcmp(temp -> data, x) == 0) return temp;
		else
		{
			temp = temp -> link;
		}
	}
	while(temp != CL -> head);
	return NULL;
}


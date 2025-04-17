#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define BUF_SIZE 1024

const char* ans = "당신은 정답을 내는 사람 입니다.";
void error_handling(char* msg);


int main(int argc, char *argv[])
{
	int sock;
	struct sockaddr_in serv_adr;
	char buf[BUF_SIZE];
	
	if (argc != 3)
	{
		printf("사용법 : %s <IP> <port>\n", argv[0]);
		exit(1);
	}

	sock = socket(PF_INET, SOCK_STREAM, 0);

	if(sock == -1)
		error_handling("소켓 에러");

	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = inet_addr(argv[1]);
	serv_adr.sin_port = htons(atoi(argv[2]));

	if (connect(sock, (struct sockaddr*)&serv_adr, sizeof(serv_adr)) == -1)
		error_handling("연결 오류");

	//역할 받기
	read(sock, buf, BUF_SIZE);
	if (strncmp(buf, ans, strlen(ans)) == 0)
	{
		printf("당신은 정답자 입니다.\n정답을 영어로 입력하세요 : ");
		fgets(buf, BUF_SIZE, stdin);
		buf[strcspn(buf,"\n")] = 0;
		write(sock, buf, strlen(buf));

		while(1)
		{
			memset(buf, 0, BUF_SIZE);
			int len = read(sock, buf, BUF_SIZE);
			if (len <= 0)
			{
				printf("[정답자] 서버와 연결 종료\n");
				break;
			}

			buf[len] = 0;
			printf("질문 수신 : %s\n", buf);
			if(strstr(buf, "게임을 종료합니다.") != NULL)
			{
				printf("[알림] 게임이 종료되었습니다.\n");
				break;
			}

			printf("-> 예/아니오/모름 : ");
			fgets(buf, BUF_SIZE, stdin);
			buf[strcspn(buf, "\n")] = 0;
			write(sock, buf, strlen(buf));
		}
	}
	else
	{
		printf("당신은 질문자 입니다.\n");
		int slen = read(sock, buf, BUF_SIZE);
		buf[slen] = 0;
		printf("%s\n", buf);


		while(1)
		{
			printf("질문 또는 '정답:정답' 입력(정답은 영어입니다.) : ");
			memset(buf, 0, BUF_SIZE);
			fgets(buf, BUF_SIZE, stdin);
			if (strcmp(buf, "\n") == 0)
			{
				printf("[입력없음] 다시 입력해주세요.\n");
				continue;
			}

			buf[strcspn(buf, "\n")] = 0;
			write(sock, buf, strlen(buf));
			printf("[질문 전송 완료]\n");
			printf("[응답 대기중...]\n");

			int len = read(sock, buf, BUF_SIZE - 1);
			buf[len] = 0;
			printf("정답자 응답 : %s\n", buf);

			if(strstr(buf, "게임을 종료합니다.") != NULL)
			{
				printf("[알림] 게임이 종료되었습니다.\n");
				break;
			}
		}
	}

	close(sock);
	printf("프로그램을 종료합니다.\n");
	return 0;
}

void error_handling(char * msg)
{
	fputs(msg, stderr);
	fputs("\n", stderr);
	exit(1);
}

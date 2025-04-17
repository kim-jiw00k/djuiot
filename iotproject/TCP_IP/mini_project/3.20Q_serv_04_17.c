#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUF_SIZE 1024

void error_handling(char* msg);
const char *ans = "당신은 정답을 내는 사람 입니다.\n";
const char *que = "당신은 질문을 하는 사람 입니다.\n정답은 영어 입니다.\n";
const char *GUESS = "정답:";

int main(int argc, char* argv[])
{
	int serv_sock, clnt1_sock, clnt2_sock;
	struct sockaddr_in serv_adr, clnt_adr;
	socklen_t clnt_adr_sz = sizeof(clnt_adr);
	char buf[BUF_SIZE];

	serv_sock = socket(PF_INET, SOCK_STREAM, 0);
	if (serv_sock == -1)
		error_handling("소켓 에러");

	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_adr.sin_port = htons(atoi(argv[1]));

	if (argc != 2)
	{
		printf("사용법 : %s <port>\n", argv[0]);
		exit(1);
	}

	if (bind(serv_sock, (struct sockaddr*)&serv_adr, sizeof(serv_adr)) == -1)
		error_handling("주소할당 에러");
	if (listen(serv_sock , 2) == -1)
		error_handling("연결 요청 에러");

	printf("서버 실행중 ... 클라이언트 연결 대기중\n");

	clnt1_sock = accept(serv_sock, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);
	write(clnt1_sock, ans, strlen(ans));
	printf("정답자 연결 완료\n");

	clnt2_sock = accept(serv_sock, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);
	write(clnt2_sock, que, strlen(que));
	printf("질문자 연결 완료\n");

	//정답 수신
	read(clnt1_sock, buf, BUF_SIZE);
	buf[strcspn(buf, "\n")] = 0;	//개행 제거
	char answer[BUF_SIZE];
	strcpy(answer, buf);
	printf("정답(영어로 작성) : %s\n", answer);

	char start_msg[] = "정답이 정해졌습니다.\n게임을 시작합니다.\n질문을 입력하세요.\n";
	write(clnt2_sock, start_msg, strlen(start_msg));

	while(1)
	{
		memset(buf, 0, BUF_SIZE);
		int len = read(clnt2_sock, buf, BUF_SIZE);
		if (len <= 0)
			break;
		buf[len] = 0;

		// 정답시도 처리
		if (strncmp(buf, GUESS, strlen(GUESS)) == 0)
		{
			char user_guess[BUF_SIZE];
			strcpy(user_guess, buf + strlen(GUESS));
			user_guess[strcspn(user_guess, "\n")] = 0;

			if (strcmp(user_guess, answer) == 0)
			{
				write(clnt2_sock, "정답입니다!\n게임을 종료합니다.\n", strlen("정답입니다!\n게임을 종료합니다.\n"));
				write(clnt1_sock, "질문자가 정답을 맞췃습니다!\n게임을 종료합니다.\n",strlen("질문자가 정답을 맞췃습니다!\n게임을 종료합니다.\n"));
				break;
			}
			else
			{
				write(clnt2_sock, "정답이 아닙니다.\n", strlen("정답이 아닙니다\n"));
				continue;
			}
		}

		//질문자 -> 질문
		int qlen = len;
		printf("[서버] 정답자에게 질문 전달 완료 (%d바이트)\n", len);
		write(clnt1_sock, buf, len);
		printf("[서버] 질문 수신 : %s\n", buf);
		

		//정답자 -> 응답
		int alen = read(clnt1_sock, buf, BUF_SIZE);
		buf[alen] = 0;
		write(clnt2_sock, buf, alen);
		printf("[서버]질문에 대한 답변 : %s\n",buf);
		printf("[서버]질문자에게 응답 전달 완료 (%d 바이트)\n", alen);
	}
	
	close(clnt1_sock);
	close(clnt2_sock);
	close(serv_sock);

	return 0;
}

void error_handling(char* msg)
{
	fputs(msg, stderr);
	fputs("\n", stderr);
	exit(1);
}

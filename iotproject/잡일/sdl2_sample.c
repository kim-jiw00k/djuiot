#include <SDL2/SDL.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    // SDL 초기화
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL 초기화 오류: %s\n", SDL_GetError());
        return 1;
    }

    // 창 생성
    SDL_Window* window = SDL_CreateWindow("SDL2 예제", 
                                          SDL_WINDOWPOS_UNDEFINED, 
                                          SDL_WINDOWPOS_UNDEFINED, 
                                          640, 480, 
                                          SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("윈도우 생성 오류: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    // 렌더러 생성
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("렌더러 생성 오류: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // 메인 루프
    int running = 1;
    SDL_Event event;
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = 0;
            }
        }

        // 화면 지우기
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // 검은색
        SDL_RenderClear(renderer);

        // 렌더링하기
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // 빨간색
        SDL_RenderDrawLine(renderer, 100, 100, 200, 200); // 선 그리기

        // 화면 업데이트
        SDL_RenderPresent(renderer);
    }

    // 자원 해제
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

SDL_Texture *loadTexture(const char *file){
 SDL_Surface *surface;
 SDL_Texture *texture;

 surface = SDL_LoadIMG(file);
 if(surface == NULL){
  printf("%s파일을 읽을 수 없습니다.\n", file);
  return NULL;
 }

 texture = SDL_CreateTextureFromSurface(renderer, surface);
 if(texture == NULL){
  printf("텍스쳐를 생성할 수 없습니다.\n");
 }

 SDL_FreeSurface(surface);

 return texture;
}
void drawTexture(SDL_Renderer *renderer,int x,int y,SDL_Texture *texture){
 SDL_Rect src,dst;

 src.x = 400; 
 src.y = 70;
 SDL_QueryTexture(texture, NULL, NULL, &src.w, &src.h);

 dst.x = x;
 dst.y = y;
 dst.w = src.w;
 dst.h = src.h;

 SDL_RenderCopy(renderer, texture, &src, &dst);
}



bool quit = false;
SDL_Event event;

SDL_Texture *texture;

texture = loadTexture("image.jpg");
texture1 = loadTexture("image1.jpg");

while(!quit){
  while(SDL_PollEvent(&event)){
   switch(event.type){
   case SDL_QUIT:
    quit = true;
    break;
   }
  }
  {
   drawTexture(renderer, 120,70, texture);
   drawTexture(renderer, 250,70, texture1);
   SDL_RenderPresent(renderer);
  }
  SDL_Delay(1);
 }

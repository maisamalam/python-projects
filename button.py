import pygame
import os
pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')
BLACK= (0,0,255)
first_img = pygame.image.load(os.path.join('Assets','start_btn.png')).convert_alpha()
second_img = pygame.image.load(os.path.join('Assets','exit_btn.png')).convert_alpha()
third_img = pygame.image.load(os.path.join('Assets','loginbutton.png')).convert_alpha()
font = pygame.font.SysFont("TimesNewRoman", 17)

game_start = False
def draw_text(text,font,BLACK,x,y):
    img = font.render(text,True,BLACK)
    screen.blit(img,(x,y))
class Button():
    def __init__(self,x,y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        draw_text("WELCOME TO SOCCER GAME! IF YOURE NEW CLICK START! ", font, BLACK,10,20)
        draw_text("IF YOU'VE PLAYED BEFORE CLICK LOGIN! ", font, BLACK,40,35)

        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                if event.type==pygame.QUIT:
                    run =False
        #pygame.display.update()
        action = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked== False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image,(self.rect.x,self.rect.y))    
        return action

start_button = Button(45,200,first_img, 0.8)
exit_button = Button(280, 200,second_img, 0.8)
login_button = Button(150,300,third_img, 0.8)



run = True
while run:

    screen.fill((202,228,241))

    if start_button.draw(screen):
        print("START")

    if exit_button.draw(screen):
        run = False
        #print("EXIT")

    login_button.draw(screen)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

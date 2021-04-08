import pygame
import sys
#khoi tao
pygame.init()
#width,height
WIDTH,HEIGHT=1200,700
# khai bao screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
# tai anh vao mot bien
bg=pygame.image.load('./img/1719689.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
charater=pygame.image.load('./img/hello.png')
charater=pygame.transform.scale(charater,(300,150))
charater_rect=charater.get_rect(center=(600,430))
# bat dau game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    screen.blit(charater,charater_rect)
    pygame.display.update()

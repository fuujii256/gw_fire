import sys
import random
import cv2
import numpy as np
import pygame
import time



def main(): # メイン

    img_bg = [ 
        pygame.image.load("image/Fire 0.png"),
        pygame.image.load("image/Fire 1.png"),            
        pygame.image.load("image/Fire 2.png"),
        pygame.image.load("image/Fire 3.png"),
        pygame.image.load("image/Fire 4.png"),
        pygame.image.load("image/Fire 5.png"),
        pygame.image.load("image/Fire 6.png"),
        pygame.image.load("image/Fire 7.png"),
        pygame.image.load("image/Fire 8.png"),
        pygame.image.load("image/Fire 9.png"),
        pygame.image.load("image/Fire 10.png"),
        pygame.image.load("image/Fire 11.png"),
        pygame.image.load("image/Fire 12.png"),
        pygame.image.load("image/Fire 13.png"),
        pygame.image.load("image/Fire 14.png"),
        pygame.image.load("image/Fire 15.png"),
        pygame.image.load("image/Fire 16.png"),
        pygame.image.load("image/Fire 17.png"),
        pygame.image.load("image/Fire 18.png"),
        pygame.image.load("image/Fire 19.png"),
        pygame.image.load("image/Fire 20.png")            
    ]
            
            
    img_scn_bg0= pygame.image.load('image/karibg.png') 

    pygame.init()
    pygame.display.set_caption("Game watch Fire")

    scn_width = 1024 
    scn_height = 768
    
    screen = pygame.display.set_mode((scn_width, scn_height))
    scr =pygame.Surface((scn_width,scn_height),flags=pygame.SRCALPHA)
    
    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    
    clock = pygame.time.Clock()

   
    pwidth = 1024
    pheight = 768      #画像表示サイズの変更

    counter = 0 
    pattern_MAX = 24
    player_pos = 2    #
    char_ptn = [0,1,1,1,1,2,3,3,3,4,4,4,4,5,6,6,6,7,7,8,9,9,10,11,11]
    char_ang = [0,0,30,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    char_pos_x=[0,350,345,350,360,380,395,405,415,425,440,455,460,480,
                500,520,540,555,575,590,605,620,655,685,0,0]
    char_pos_y=[0,270,295,330,365,410,370,335,300,270,305,340,375,410,
                375,340,305,340,375,410,375,340,375,370,0,0]

    
    while True: 
        screen.blit(img_scn_bg0,[0,0])
#       screen.blit(img_bg[0], [0,0])

        i = 0   
        while i < pattern_MAX+1:
            img = pygame.transform.rotozoom(img_bg[char_ptn[i]],char_ang[i],1.0)
            screen.blit(img,[char_pos_x[i],char_pos_y[i]]) 
            i += 1

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((pwidth, pheight), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((pwidth, pheight))
                if event.type == pygame.K_F3:
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        clock.tick(24)

if __name__ == '__main__':
    main()




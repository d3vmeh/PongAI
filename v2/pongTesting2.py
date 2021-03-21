import pygame
from pygame.locals import *
import time
import random
import keras
from keras.models import load_model
import numpy as np


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640,480))
screen.fill(black)
pygame.display.set_caption("Pong")
pygame.display.update()


#actions: rightpaddledown = 0, rightpaddleup =1, rightpaddlestay = 2


#file = open("pongdata.csv",'a')
#file.write("circlex,circley,paddley,currentaction\n")


def display_score(msg,p,q):
    font = pygame.font.SysFont("comicsansms",70)
    textsurface = font.render(msg,True,white)
    screen.blit(textsurface,(p,q))

def game():

    #screen = pygame.display.set_mode((640,480))
    
    clock = pygame.time.Clock()
    x = 0
    y = 240

    x1 = 630
    y1 = 240
    # pygame.draw.rect(screen,blue,(x,y,10,50),5)
    # pygame.draw.rect(screen,red,(x1,y1,10,50),5)

    circlex = 320
    circley = 240
    # pygame.draw.circle(screen,white,(circlex,circley),20,5)
    xchange = 4     #Was previously 3 for both
    ychange = 4

    rightpaddleup = 0
    rightpaddledown = 0

    leftpaddleup = 0
    leftpaddledown = 0

    count1 = 0
    count2 = 0

    smallrectx = 320
    smallrecty = 10
    # beep = pygame.mixer.Sound("/Users/dmehra/Documents/Pythonl/Pong/ping_pong_8bit_beeep.ogg")
    # peep = pygame.mixer.Sound("/Users/dmehra/Documents/Pythonl/Pong/ping_pong_8bit_peeeeeep.ogg")
    # plop = pygame.mixer.Sound("/Users/dmehra/Documents/Pythonl/Pong/ping_pong_8bit_plop.ogg")
    screen.fill(black)
    display_score(str(count1),120,10)
    display_score(str(count2),440,10)
    
        
    
    pygame.draw.rect(screen,white,(x,y,10,50),0)
    pygame.draw.rect(screen,white,(x1,y1,10,50),0)
    pygame.draw.circle(screen,white,(circlex,circley),20)
    pygame.display.update()
    time.sleep(1)


    previousaction = 0
    currentaction = 0

    #model = load_model("pongmodel.h5")
    model = load_model("pongmodel2.h5")
    previouspaddley=y1
    while True:
        pygame.display.update()
        
        # circlex += 1
        # circley += 1
        # if circley>=460:
        #     circley -= 1
        # if circlex>=620:
        #     circlex -= 1
        # if circlex>=620 and circley>=460:
        #     circlex -= 1
        #     circley -= 1


        circlex += xchange
        circley += ychange
        clock.tick(100)
        # if circlex>= 610:
        #     xchange = -5
        # if circlex<=30:
        #     xchange = 5

        #Conditions for ball hitting the paddle
        if x<circlex-20<x+10 and y-20<circley<y+70: #Left paddle
            #beep.play()
            xchange = 4
            
        if x1<circlex+20<x1+10 and y1-20<circley<y1+70: #Right paddle
            #beep.play()
            xchange = -4
            
        if count1 == 5 or count2 == 5:
            screen.fill(black)
            message = 'Game Over'
            #font = pygame.font.Font("/Users/dmehra/Documents/Pythonl/Pong/myresources/fonts/Papyrus.TTF",50)
            font = pygame.font.SysFont("comicsansms",50)
            gameover = font.render(message,True,red)
            screen.blit(gameover,(95,200))  #Size of the entire text is 450(x),and 640-450 = 190, and 190/2 = 95
            pygame.display.update()
            break
            #menu()
        else:
            
            if circlex>x1:
                print("scored at",circley)

                circlex = 320
                circley = 240
                #peep.play()
                count1 = count1+1
                display_score(str(count1),120,10)
                xchange = -5
                reward = -1
                continue
            if circlex-20<x:
                circlex = 320
                circley = 240
                #peep.play()
                count2 = count2+1
                display_score(str(count2),440,10)
                xchange = 5
                #reward = 100
                #stringtowrite = str(circlex)+","+str(circley)+","+str(y1)+","+str(currentaction)+"\n"
                continue

            if circley+20>480:
                #xchange = -3
                #plop.play()
                ychange = -4
                continue
            
            if circley-20<0:
                #plop.play()
                ychange = 4
                continue


        if rightpaddleup == 1:
            previouspaddley = y1
            y1 -= 15    #Was previously 5,10
            previousaction = 1
        if rightpaddledown == 1:
            previouspaddley = y1
            y1 += 15
            previousaction = 0
        if leftpaddleup == 1:
            y -= 15
        if leftpaddledown == 1:
            y += 15
        
        # if rightpaddleup == 1 and rightpaddledown == 1:
        #     print("Previously was still")
        #     a = np.array([circley,y1,2])
        #else:
        a = np.array([circley,y1,previousaction])

        #print(a.shape)
        a = np.reshape(a,(1,3))
        print(a.shape)
        predictions = model.predict(a)

        prediction = np.argmax(predictions[0])

        #print(predictions[0])

        
        if prediction == 0:
            rightpaddledown = 1
            rightpaddleup = 0
            print("down")
            #y1 += 15

        if prediction == 1:
            rightpaddleup = 1
            rightpaddledown = 0
            print("up")
            #y -= 15
        # else:
        #     rightpaddleup = 1
        #     rightpaddledown = 1
        #     print(prediction,"still")


        #Conditions for moving the paddles
       
        # if y<0 or y>430:
        #     y = 240
        # if y1<0 or y1>430:
        #     y1 = 240

        randomleftaction = random.randint(0,25)

        # if 0<randomleftaction<10:
        #     leftpaddledown = 1
        # if 10<randomleftaction<20:
        #     leftpaddleup = 1
        # if 20<randomleftaction<25:
        #     leftpaddledown = 0
        #     leftpaddleup = 0



        


        if y<0:
            y = 0
        if y>430:
            y = 430
        if y1<30:
            y1 = 30
        if y1>410:
            y1 = 410
        circlex += xchange


        if circlex+20>=x1 and y1<circley<y1+50:
            print("hit ball")
            #stringtowrite = str(circlex)+","+str(circley)+","+str(y1)+","+str(currentaction)+"\n"
            #file.write(stringtowrite)


        screen.fill(black)
        for i in range (10,430,50):
            pygame.draw.rect(screen,white,(smallrectx,i,10,40),0)
        
        display_score(str(count1),120,10)
        display_score(str(count2),440,10)
        pygame.draw.rect(screen,white,(x,y,10,50),0)
        pygame.draw.rect(screen,white,(x1,y1,10,50),0)
        pygame.draw.circle(screen,white,(circlex,circley),20)
        
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                # if event.key == K_UP:
                #     rightpaddleup = 1
                    
                # elif event.key == K_DOWN:
                #     rightpaddledown = 1
                
                if event.key == K_w:
                    leftpaddleup = 1

                elif event.key == K_s:
                    leftpaddledown = 1

            elif event.type == KEYUP:
                # if event.key == K_UP:
                #     rightpaddleup = 0
                    
                # elif event.key == K_DOWN:
                #     rightpaddledown = 0
                
                if event.key == K_w:
                    leftpaddleup = 0

                elif event.key == K_s:
                    leftpaddledown = 0

for i in range(3):
    game()


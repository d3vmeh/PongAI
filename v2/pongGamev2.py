import pygame
from pygame.locals import *
import time
import random



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


file = open("pongdata2.csv",'a')
#file.write("circley,paddley,currentaction\n")


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
    
    global upcount
    global downcount
    global staycount
    upcount = 0
    downcount = 0
    staycount = 0
    
    while True:
        pygame.display.update()
        
        # circlex += 1
        # circley += 1
        # if circley>=460:
        #     circley -= 1
        # if circlex>=620:
        #     circlex -= 1
        # if circlex>=620 and circley>=460:
        #     cwait wuuirclex -= 1
        #     circley -= 1


        circlex += xchange
        circley += ychange
        clock.tick(190)
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
                #stringtowrite = str(circley)+","+str(y1)+','+str(previousaction)+','+str(currentaction)+"\n"
                #file.write(stringtowrite)
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


        if ychange>0 and xchange>0 and circley+20<430 and circley-20>0: #and y1<circley<y1+50:

        
            #print("Going down")
            rightpaddledown = 1
            rightpaddleup = 0
            currentaction = 0
            if y1<circley+20<y1+50 or y1<circley-5<y1+50:
                # rightpaddledown = 0
                # rightpaddleup = 0
                rightpaddledown = 1
                rightpaddleup = 1
                #currentaction = 2
                currentaction = 0
                staycount += 1
                #print("stopped going downf")
            
        if ychange<0 and xchange>0 and circley+20<430 and circley-20>0: #and y1<circley<y1+50:
            #print("Going up")
            rightpaddleup = 1
            rightpaddledown = 0
            currentaction = 1
            if y1<circley-20<y1+50 or y1<circley+5<y1+50:
                # rightpaddleup = 0
                # rightpaddledown = 0
                rightpaddledown = 1
                rightpaddleup = 1
                #currentaction = 2
                currentaction = 1
                staycount += 1 
                #print("Stopped going up")



        #Conditions for moving the paddles
        if rightpaddleup == 1:
            y1 -= 15    #Was previously 5,10
            previousaction = 1
            upcount += 1
        if rightpaddledown == 1:
            y1 += 15
            downcount += 1
            previousaction = 0
        if leftpaddleup == 1:
            y -= 15
        if leftpaddledown == 1:
            y += 15
        # if y<0 or y>430:
        #     y = 240
        # if y1<0 or y1>430:
        #     y1 = 240

        randomleftaction = random.randint(0,25)

        if 0<randomleftaction<10:
            leftpaddledown = 1
        if 10<randomleftaction<20:
            leftpaddleup = 1
        if 20<randomleftaction<25:
            leftpaddledown = 0
            leftpaddleup = 0



        if y<0:
            y = 0
        if y>430:
            y = 430
        if y1<0:
            y1 = 0
        if y1>430:
            y1 = 430
        circlex += xchange

        #if circlex+20>=x1:
            #print("hi")

        if circlex+20>=x1 and y1<circley<y1+50:
            #print("hit ball")
            reward = 1
            stringtowrite = str(circley)+","+str(y1)+','+str(previousaction)+','+str(currentaction)+"\n"
            file.write(stringtowrite)


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
                file.close()
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

for i in range(40000):
    game()

#print(upcount,downcount,staycount)
file.close()
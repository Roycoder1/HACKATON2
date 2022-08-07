from tkinter import CENTER, font
from turtle import right, screensize
import pygame
from sys import exit
from pygame.locals import *
from pygame import mixer


pygame.init()

mixer.init()
mixer.music.load('/Users/benisti/Desktop/Hackaton2/music.mp3')
mixer.music.play()
screen_width,screen_height = 1024,736
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Bestgame')
clock=pygame.time.Clock()
text_font=pygame.font.Font('/Users/benisti/Downloads/Dameron-Font (1)/dameron.ttf',50)
test_surface = pygame.image.load('/Users/benisti/Desktop/map1.png')

text_surface=text_font.render('Rivals', False, 'Red')

score_rect=text_surface.get_rect(center = (300,50))

#Player 1 : Movement
player_walk1 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/Picture1.png').convert_alpha()
player_walk2 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerwalk2.png').convert_alpha()
player_walk3 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerwalk3.png').convert_alpha()
player_walk4 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerwalk4.png').convert_alpha()
player_walk5 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerwalk5.png').convert_alpha()
player_walk6 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerwalk6.png').convert_alpha()
reverseChar = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverse1.png').convert_alpha()
reverse2 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverse2.png').convert_alpha()
reverse3 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverse3.png')
player_reverse= [reverseChar,reverse2,reverse3]
player_walk = [player_walk1,player_walk2,player_walk3,player_walk4,player_walk5,player_walk6]
player_index = 0
player_surf = player_walk[player_index]
player_jump = pygame.image.load('/Users/benisti/Desktop/Hackaton2/playerjump.png').convert_alpha()
player_rectangle = player_surf.get_rect(midbottom=(100,730))
player_gravity = 0





#Move variable

moveLeftRight = 0
moveLeft= False
moveRight = False

# Variable use in a while loop to implement bullets
bulletgroup= pygame.sprite.Group()

# pvbarplayer1 = text_font.render('PV :100', False, 'Red')
# test_surface.blit(pvbarplayer1,(00,50))



# Player2


enemy_index = 0
enemy_gravity=0
moveLeftRightPlayer2 = 0
moveLeftPlayer2= False
moveRightPlayer2 = False

enemy_surface= pygame.image.load('/Users/benisti/Desktop/Hackaton2/player2.png').convert_alpha()
player2_walk1 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/player2walk3.png').convert_alpha()
reversep2 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverseplayer2.png').convert_alpha()
reversep2walk2 = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverseplayer2w2.png').convert_alpha()
player2jumpright: pygame.image.load('/Users/benisti/Desktop/Hackaton2/p2jumpright.png').convert_alpha()
player2jumpleft: pygame.image.load('/Users/benisti/Desktop/Hackaton2/p2jumpleft.png').convert_alpha()

p2w2 = [enemy_surface,player2_walk1]
enemy_rect = enemy_surface.get_rect(midbottom =(850,760))
moveLeftRightPlayer2 = 850
pvPlayer2 = 100

fireball= pygame.sprite.Group()




def player_animation():
    global player_surf,player_index

    if player_rectangle.bottom<710:
        player_surf=player_jump
          
    else:
        player_index+=0.2
        if player_index>=len(player_walk): player_index = 0
        player_surf= player_walk[int(player_index)]
        
def reverse1():
    global player_surf,player_index
    
    player_index+=0.2
    if player_index>=len(player_reverse): player_index = 0
    player_surf = player_reverse[int(player_index)]
    
        # player_surf = reverse2

def player2_walk():

    global enemy_surface,enemy_index

    if enemy_rect.bottom<710:
        enemy_surface=pygame.image.load('/Users/benisti/Desktop/Hackaton2/p2jumpleft.png').convert_alpha()

    else:
        enemy_index +=0.1
        if 0<1:
         enemy_surface = player2_walk1

def reverseplayer2():

    global enemy_surface,enemy_index
    if enemy_rect.bottom<710:
        enemy_surface=pygame.image.load('/Users/benisti/Desktop/Hackaton2/p2jumpright.png').convert_alpha()
    else:
     if 0<1 :
        enemy_surface = reversep2walk2

class Player (pygame.sprite.Sprite):
   
    def __init__(self):
        super().__init__()
        self.image = player_walk[player_index]
        self.rect = player_rectangle
        self.image2 = pygame.Surface((40,40))
        self.image2.fill((240,240,240))
        self.rect2 = self.image2.get_rect(center = (400,400))
        self.pvplayer1 = 100
        self.maximumHealth = 100
        self.health_bar_length = 400
        self.health_ratio =self.maximumHealth/self.health_bar_length

    # def update(self):
    #      self.basic_health()
        
         
    
    def createBullet(self):
        return Bullet(self.rect.x,self.rect.y)
    
    def getDamage(self,amount):
        if self.pvplayer1>0:
            player1.pvplayer1 -=amount 
        if self.pvplayer1<= 0:
            player1.pvplayer1 = 0 
        
    def get_health(self,amount):
        if player1.pvplayer1<player1.maximumHealth:
            player1.pvplayer1+=amount
        if player1.pvplayer1>= self.maximumHealth:
            player1.pvplayer1 = self.maximumHealth
    
    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0),(10,10,player1.pvplayer1/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(10,10,player1.health_bar_length,25),4)
       

player_test = pygame.sprite.GroupSingle(Player())
group_player =pygame.sprite.GroupSingle()
player1 = Player()
group_player.add(player1)
# BLUE_GREEN = (111, 196, 169)
# text_font2=pygame.font.Font('/Users/benisti/Downloads/Dameron-Font (1)/dameron.ttf',50)
# bar_surface = text_font2.render(f'PV:   {player1.pvplayer1}', False, BLUE_GREEN)
# bar_rect = bar_surface.get_rect(midtop = (400,70))
# screen.blit(bar_surface, bar_rect)



def display_gameoverP2():
    'Display the gameover window'
    gameover_surf =test_surface
    gameover_surf = pygame.Surface((1024,736))
     
    text1 = gameover_surf.fill((94, 129, 162))

                
    text2= gameover_surf.get_rect(topleft = (0,0))
     
    messageGO=text_font.render('PLAYER 1 WON', False, 'Red')

    score_rect=messageGO.get_rect(center = (512,300))
    test_surface.blit(gameover_surf,text2)
    test_surface.blit(messageGO,score_rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = player_walk1
        self.image =pygame.image.load('/Users/benisti/Downloads/bullet.png').convert_alpha()
        # self.image.fill((255,0,0))
        self.rect = self.image.get_rect(midright = (pos_x+145,pos_y+50))
        
        
    def update(self):
        self.rect.x +=9
        # players2.sprite.basic_health()
        player2.basic_health()
        collide2 = self.rect.colliderect(player2.rect)
        
        if collide2:
           
            players2.sprite.getDamage(6.667)

            player2.basic_health()
            # player1.pvplayer1 -= 50
            
            if player2.pvplayer2==0 or player2.pvplayer2<0:
                
                display_gameoverP2()
            

        if collide2:
            self.kill()
        
    def createBullet(self):
        return Bullet()

bullet = Bullet(enemy_rect.x,enemy_rect.y)

class Player2 (pygame.sprite.Sprite):
     
    def __init__(self):
        super().__init__()
        self.image = enemy_surface
        self.rect = enemy_rect
        self.image2 = pygame.Surface((40,40))
        self.image2.fill((240,240,240))
        self.rect2 = self.image2.get_rect(center = (400,400))
        self.pvplayer2 =100
        self.maximumHealth = 100
        self.health_bar_length = 400
        self.health_ratio =self.maximumHealth/self.health_bar_length

    def update(self):
         self.basic_health()
         
    
    def createFire(self):
        return FireBall(self.rect.x,self.rect.y)

    def getDamage(self,amount):
        if self.pvplayer2>0:
            player2.pvplayer2 -=amount 
        if self.pvplayer2<=0:
            player2.pvplayer2 = 0 
    def get_health(self,amount):
        if player2.pvplayer2<player2.maximumHealth:
            player2.pvplayer2+=amount
        if player2.pvplayer2>= self.maximumHealth:
            self.pvplayer2 = self.maximumHealth

    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0),(600,10,player2.pvplayer2/self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(600,10,player2.health_bar_length,25),4)


players2=pygame.sprite.GroupSingle(Player2())
group_player2 = pygame.sprite.GroupSingle()    
player2 = Player2()
group_player2.add(player2)

def display_gameover():
     'Display the gameover window'
     gameover_surf =test_surface
     gameover_surf = pygame.Surface((1024,736))
     
     text1 = gameover_surf.fill((94, 129, 162))

                
     text2= gameover_surf.get_rect(topleft = (0,0))
     
     messageGO=text_font.render('PLAYER 2 WON', False, 'Red')

     score_rect=messageGO.get_rect(center = (512,300))
     test_surface.blit(gameover_surf,text2)
     test_surface.blit(messageGO,score_rect)
    #  player_surf.blit(0,0)



class FireBall(pygame.sprite.Sprite):
    'Create fireball'
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = enemy_surface
        self.image =pygame.image.load('/Users/benisti/Desktop/Hackaton2/fireball.png').convert_alpha()
        # self.image.fill((255,0,0))
        self.rect = self.image.get_rect(midleft = (pos_x-10,pos_y+60))
        
    def update(self):
        self.rect.x -=9
        player1.basic_health()
        # player_test.sprite.basic_health()
        collide1 = self.rect.colliderect(player1.rect)
        
        if collide1:
            player1.basic_health()
            player_test.sprite.getDamage(6.667)
            # player1.basic_health()
            # player1.pvplayer1 -= 50
            # print(player1.pvplayer1)
            if player1.pvplayer1==0 or player1.pvplayer1<0:
                display_gameover()

        if collide1:
            self.kill()
    def createFire(self):
        return FireBall()


firet = FireBall(player_rectangle.x,player_rectangle.y)





#event loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type== pygame.KEYDOWN:
            if event.key ==pygame.K_w and player_rectangle.bottom >= 700:
                player_gravity=-20
            if event.key== pygame.K_d:
                moveRight = True
                
               
            if event.key== pygame.K_a:
                moveLeft = True
            
            if event.key == pygame.K_s:
                player_test.sprite.get_health(200)
                
            if event.key == pygame.K_SPACE:
                
                bulletgroup.add(player1.createBullet())
                # player2.update()
                # pvplayer2 =100
                
                # if bulletgroup.update(): #event qui voit si y a une collision et qui me retourne cb le perso a ete touche
                #      player2.pvplayer2-=50
                     
            #PLAYER2
            if event.key ==pygame.K_UP and enemy_rect.bottom >= 700:
                enemy_gravity=-20
            if event.key== pygame.K_RIGHT:
                moveRightPlayer2 = True
                
                
                reverseplayer2()


            if event.key== pygame.K_LEFT:
                moveLeftPlayer2 = True
                
                player2_walk()

            if event.key == pygame.K_RSHIFT :
                
                
               
                # player1.update()
               
                enemy_surface = pygame.image.load('/Users/benisti/Desktop/Hackaton2/firecharacter.png').convert_alpha()

                fireball.add(player2.createFire())
                # player1.update()
                
                

                
              
        elif event.type == pygame.KEYUP:

        

            if event.key== pygame.K_d:
                moveRight = False

            if event.key== pygame.K_a:
                moveLeft = False
            
            #Player2


                
                
                # player1.getDamage(100)

            if event.key== pygame.K_RIGHT:
                moveRightPlayer2 = False
                enemy_surface = pygame.image.load('/Users/benisti/Desktop/Hackaton2/reverseplayer2.png').convert_alpha()


            if event.key== pygame.K_LEFT:
                moveLeftPlayer2 = False
                enemy_surface= pygame.image.load('/Users/benisti/Desktop/Hackaton2/player2.png').convert_alpha()
        
    if  moveRight: 
        moveLeftRight +=8
        player_animation()
    if moveLeft:
        moveLeftRight -=8
        reverse1()
        


    
    #player2
 

    if  moveRightPlayer2: 
        moveLeftRightPlayer2 += 8


    if moveLeftPlayer2:
        moveLeftRightPlayer2-=8
       

               
    screen.blit(test_surface,(0,0))
    screen.blit(text_surface,(400,50))
    
 
    #player

    player_rectangle.x = moveLeftRight
    player_gravity +=1
    player_rectangle.y+=player_gravity
    if player_rectangle.bottom >= 710:
        player_rectangle.bottom=710
   
    screen.blit(player_surf,player_rectangle)
    bulletgroup.draw(screen)
    bulletgroup.update()

   # Player2
    fireball.draw(screen)
    fireball.update()
    screen.blit(enemy_surface,enemy_rect)
    enemy_rect.x = moveLeftRightPlayer2 
    
    enemy_gravity +=1
    enemy_rect.y+=enemy_gravity
    if enemy_rect.bottom>729:
        enemy_rect.bottom  = 730
        
    firstbarrier = pygame.Surface((50,250))
    firstrect = firstbarrier.get_rect(midbottom = (600,600))
    collide = pygame.Rect.colliderect(enemy_rect, firstrect)
    # if collide:   #PROBLEM COLLISION NE PAS ENLEVER
    #     enemy_rect = firstrect

    # if enemy_rect!=firstrect:
    #     enemy_rect  = enemy_rect

    
   
    pygame.display.update()
    clock.tick(60)# Set 60 fps


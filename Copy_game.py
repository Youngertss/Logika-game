from pygame import *

white = color.Color("#FFFFFF")
black = color.Color("#0083ff")
width = 242

#классы
class Player(sprite.Sprite):
    def __init__(self,player_imaged,player_imageu,player_imagel,player_imager, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.imaged = transform.scale(image.load(player_imaged), (size_x, size_y))
        self.imageu = transform.scale(image.load(player_imageu), (size_x, size_y))
        self.imagel = transform.scale(image.load(player_imagel), (size_x, size_y))
        self.imager = transform.scale(image.load(player_imager), (size_x, size_y))
        self.speed_def=player_speed
        self.speed = player_speed+10
        self.list_img=[self.imaged,self.imageu,self.imagel,self.imager]
        self.s=0
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.imaged.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.list_img[self.s], (self.rect.x, self.rect.y))

    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        global width
        global ch
        keys = key.get_pressed()
            
        if keys[K_UP] and z !=2:
            self.rect.y -= self.speed
            self.s=1
        elif keys[K_w] and z !=2:
            self.rect.y -= self.speed
            self.s=1
            
        if keys[K_DOWN] and z !=1:
            self.rect.y += self.speed
            self.s=0
        elif keys[K_s] and z !=1:
            self.rect.y += self.speed
            self.s=0

        if keys[K_LEFT] and x!=2:
            self.rect.x -= self.speed
            self.s=2
        elif keys[K_a] and x!=2:
            self.rect.x -= self.speed
            self.s=2
        
        if keys[K_RIGHT] and x !=1 :
            self.rect.x += self.speed
            self.s=3
        elif keys[K_d] and x !=1 :
            self.rect.x += self.speed
            self.s=3
        if keys[K_LSHIFT] and keys[K_LEFT] or keys[K_LSHIFT] and keys[K_a] or keys[K_LSHIFT] and keys[K_RIGHT] or keys[K_LSHIFT] and keys[K_d] or keys[K_LSHIFT] and keys[K_UP] or keys[K_LSHIFT] and keys[K_w] or keys[K_LSHIFT] and keys[K_DOWN] or keys[K_LSHIFT] and keys[K_s]:
            self.speed = self.speed_def+2
            width -= 2
        elif keys[K_LSHIFT]:
            width+=1
        if width<10:
            self.speed = self.speed_def
        if not keys[K_LSHIFT]:    
            width += 1
            self.speed = self.speed_def
        if width > 242:
            width = 242
        elif width < 1:
            width = 1

        if rv==1:
            self.rect.x=40
        if rv==2:
            self.rect.x=1780


class Wall(sprite.Sprite):
    def __init__(self,width,height,x,y,col1,col2,col3):
        sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.image=Surface((self.width,self.height))
        self.image.fill((self.col1,self.col2,self.col3))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#нужные функции
def add_walls1_to_groups():
    for i in range(len(wr1l)):
        wallsR.add(wr1l[i])
    for i in range(len(wl1l)):
        wallsL.add(wl1l[i])
    for i in range(len(wu1l)):
        wallsU.add(wu1l[i])
    for i in range(len(wd1l)):
        wallsD.add(wd1l[i])

#изображения нужные
bg1_img = "bg_.png"
bg2_img = "bg.jpg"
bg_lobby_img = "lobby_bg.png"
play_img = "play.png"
quit_img="QUIT.png"

menu_img = "menu.png"
player_imgl ="pl_left.png"
player_imgr = "pl_right.png"
player_imgu = "pl_up.png"
player_imgd = "pl_down.png"

#параметры окна
win_width=1920
win_height=1040
window=display.set_mode((0,0),RESIZABLE)
display.set_caption("Logika-game")

but_menu=transform.scale(image.load(menu_img),(150, 75))
but_play=transform.scale(image.load(play_img),(200, 150))
but_quit=transform.scale(image.load(quit_img),(120, 60))
background_lbl=transform.scale(image.load(bg_lobby_img),(win_width, win_height))
background1=transform.scale(image.load(bg1_img),(win_width,win_height))
background2=transform.scale(image.load(bg2_img),(win_width,win_height))

x=0
z=0
rv=0


#спрайт игрока
geroy=Player(player_imgd,player_imgu,player_imgl,player_imgr, 250,270,120,160,15)
##############################################################################
room1w=sprite.Group()
room2w=sprite.Group()


door1=Wall(15,200,1905,400,103,51,0)
door2=Wall(15,200,0,400,103,51,0)

doorG=[]
doorG.append(door1)

wr1=Wall(15,400,1905,0,0,0,0)
wr2=Wall(15,700,1905,600,0,0,0)
wd1=Wall(1920,15,0,1025,0,0,0)
wl1=Wall(15,1040,0,0,0,0,0)
wu1=Wall(1920,15,0,0,0,0,0)

wd1_2=Wall(800,15,0,575,0,0,0)

wr1l=[wr1,wr2]
wl1l=[wl1]
wu1l=[wu1]
wd1l=[wd1]

wd2l=[wd1_2]

room1wl=[wr1,wr2,wd1,wl1,wu1,door1]
room2wl=[door2,wd1_2]

wallsR=sprite.Group()
wallsL=sprite.Group()
wallsD=sprite.Group()
wallsU=sprite.Group()
##############################################################################
ch=True
clock=time.Clock()

finish=False
speed_vis = False
run=True
game="stop"
while run:
    window.blit(background_lbl,(0,0))
    window.blit(but_play,(280,225))
    window.blit(but_quit,(310,360))


    #проверка событий
    for e in event.get():
        if e.type==QUIT:
            run=False

        if e.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            if x >= 320 and x <= 450:
                if y >= 270 and y <= 340:
                    game='start'
                    speed_vis = True
            if x >= 20 and x <= 130:
                if y >= 15 and y <= 60:
                    game='stop'
                    speed_vis = False
            if x >=320 and x <=430 and game=='stop':
                if y >= 360 and y<=410:
                    run=False

    #проверка столкновений
    if sprite.spritecollide(geroy,wallsR,False):
        x=1           
    elif sprite.spritecollide(geroy,wallsL,False):
        x=2
    else:
        x=0    
    if sprite.spritecollide(geroy,wallsD,False):
        z=1    
    elif sprite.spritecollide(geroy,wallsU,False):
        z=2        
    else:
        z=0
    #столкновение с дверью и смена комнат
    if doorG[0] == door1:
        if sprite.spritecollide(geroy,doorG,False):
            game="room2"
            doorG.remove(door1)
            doorG.append(door2)
            rv=1
        else:
            rv=0
    elif doorG[0] == door2:
        if sprite.spritecollide(geroy,doorG,False):
            game="start"
            doorG.remove(door2)
            doorG.append(door1)
            rv=2
        else:
            rv=0
    
    #отоброжение комнат и среды
    if game == "start":

        window.blit(background1,(0,0))
        window.blit(but_menu,(0,0))
        
        for i in range(len(room1wl)):
            room1w.add(room1wl[i])
        add_walls1_to_groups()

        geroy.update()
        geroy.reset()
        room1w.draw(window)
    elif game=="room2":
        window.blit(background2,(0,0))
        window.blit(but_menu,(0,0))
        geroy.update()
        geroy.reset()
        
        for i in range(len(room1wl)):
            room1wl[i].kill()
            
        for i in range(len(room2wl)):
            room2w.add(room2wl[i])
            
        room2w.draw(window)

    if speed_vis == True:
        draw.rect(window, black, [25, 560, 252, 34])
        draw.rect(window, white, [26, 561, 250, 32])
        draw.rect(window, black, [30, 565, width, 24])
                        

    display.update()
    # цикл срабатывает каждую 0.06 секунд
    clock.tick(60)
    

"""quit()
window=display.set_mode((0,0),RESIZABLE)
while ch:
    window.blit(background2,(0,0))
    for e in event.get():
        if e.type==QUIT:
            ch=False
    display.update()
    time.delay(1)"""
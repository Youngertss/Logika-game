from pygame import *
x_pl=250
y_pl=270
class GameSprite(sprite.Sprite):
    def __init__(self,player_imaged,player_imageu,player_imagel,player_imager, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.imaged = transform.scale(image.load(player_imaged), (size_x, size_y))
        self.imageu = transform.scale(image.load(player_imageu), (size_x, size_y))
        self.imagel = transform.scale(image.load(player_imagel), (size_x, size_y))
        self.imager = transform.scale(image.load(player_imager), (size_x, size_y))
        self.speed = player_speed
        self.list_img=[self.imaged,self.imageu,self.imagel,self.imager]
        self.s=0
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.imaged.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.list_img[self.s], (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        global s
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > -40:
            self.rect.x -= self.speed
            self.s=2
        if keys[K_RIGHT] and self.rect.x < win_width-60 :
            self.rect.x += self.speed
            self.s=3
        if keys[K_UP] and self.rect.y > -30:
            self.rect.y -= self.speed
            self.s=1
        if keys[K_DOWN] and self.rect.y < win_height-60:
            self.rect.y += self.speed
            self.s=0

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
        

#изображения нужные

bg_img="bg.jpg"
bg_lobby_img="lobby_bg.png"
but_play_img="play.png"

player_imgl="pl_left.png"
player_imgr="pl_right.png"
player_imgu="pl_up.png"
player_imgd="pl_down.png"

menu_img="menu.png"
#параметры окна
win_width=800
win_height=600
window=display.set_mode((win_width,win_height))
display.set_caption("Logika-game")

menu=transform.scale(image.load(menu_img),(150, 75))
play=transform.scale(image.load(but_play_img),(200, 150))
background_lbl=transform.scale(image.load(bg_lobby_img),(win_width, win_height))
background=transform.scale(image.load(bg_img),(win_width,win_height))

#спрайт игрока

geroy=Player(player_imgd,player_imgu,player_imgl,player_imgr, 250,270,60,80,5)
#спрайты стен и группы
walls1=sprite.Group()
w1=Wall(10,300,600,0,0,0,0)
w2=Wall(200,10,410,300,0,0,0)
walls1.add(w1,w2)

finish=False
run=True
game=""
while run:
    window.blit(background_lbl,(0,0))
    window.blit(play,(280,225))
    
    for e in event.get():
        if e.type==QUIT:
            run=False
    
        if e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            if pos >= (280,225) and pos <= (480, 250):
                game='start'
            if pos >= (20,10) and pos <= (130, 60):
                game='stop'
                
    
    if game == "start":
        window.blit(background,(0,0))
        window.blit(menu,(0,0))
        
        geroy.update()
        geroy.reset()
        walls1.draw(window)

            
        
        
    display.update()
    
    time.delay(10)
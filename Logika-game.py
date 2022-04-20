from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
#изображения нужные
downbg_img="dirt_bg.png"
bg_img="bg_st_night.png"
bg_lobby_img="lobby_bg.png"
but_play_img="play.png"
player_img="pers1.png"
#параметры окна
win_width=800
win_height=600
window=display.set_mode((win_width,win_height))
display.set_caption("Logika-game")

play=transform.scale(image.load(but_play_img),(200, 150))
background_lbl=transform.scale(image.load(bg_lobby_img),(win_width, win_height))
background=transform.scale(image.load(bg_img),(win_width, 500))
background_down=transform.scale(image.load(downbg_img),(win_width,450))

#спрайт игрока
geroy=Player(player_img,20,200,80,100,5)

finish=False
run=True
game=""
while run:
    window.blit(background_lbl,(0,0))
    window.blit(play,(280,225))
    
    for e in event.get():
        if e.type==QUIT:
            game=False
    
        if e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            if pos >= (280, 220) and pos <= (480, 370):
                game='start'
    
    while game == "start":
        window.blit(background,(0,0))
        window.blit(background_down,(0,280))
        
        geroy.update()
        geroy.reset()
    
    display.update()
    
    time.delay(50)
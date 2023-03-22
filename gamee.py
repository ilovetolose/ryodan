import pygame
import random
from os import path
import time


img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1280
HEIGHT = 1024
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (252, 15, 192)
PURPLE = (224, 176, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("clown sdoh")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')
# графика
background = pygame.image.load(path.join('aviapark.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join( "ryodan.jpg")).convert()
vrag_img = pygame.image.load(path.join( 'stoneisland.png')).convert()
boss_img = pygame.image.load(path.join( 'boss.png')).convert()

background_rect = background.get_rect()





def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(vrag_img, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.hp = 100

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_w]:
            self.speedy = -4
        self.rect.y += self.speedy
        if keystate[pygame.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boss_img, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


font_name = pygame.font.match_font('arial')
label = pygame.font.Font('rofl.ttf', 128)
restart_label = label.render('restart',False,(PINK))
restart_label_rect = restart_label.get_rect(topleft=(WIDTH/2,200))

def draw_text(surf, text, size, x, y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 300
    BAR_HEIGHT = 20
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
boss = Boss()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(boss)


for i in range(30):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0


# Цикл игры
running = True
gameplay = True

while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
    if gameplay:


    # Рендеринг
        screen.fill(BLACK)
        screen.blit(pygame.transform.scale(background, (1280, 1024)), background_rect)
        all_sprites.draw(screen)
        hits = pygame.sprite.spritecollide(player, mobs, False)
        score+=1
        time = draw_text(screen,'вашиочко: '+str(score), 40, WIDTH / 4, 2,WHITE)
        draw_shield_bar(screen, 1000, 40,player.hp)
        draw_text(screen, 'ваши хп', 40, 900, 20, GREEN)

    else:
        screen.fill((0,0,0))
        pygame.time.Clock()
        draw_text(screen, 'вашиочко который ты заработал: '+str(score), 40, WIDTH / 2, 2,WHITE)
        draw_text(screen, str('потрачено....'), 128 , 600, HEIGHT/ 3,WHITE)
        draw_text(screen, 'GTA RYODAN:VICEVICEVICEAVICEXD', 40, WIDTH / 2, 800,PURPLE)
        screen.blit(restart_label,restart_label_rect)

        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        all_sprites.add(boss)
        if restart_label_rect.collidepoint(pos) and pressed[0]:
            gameplay = True
            score = 0
            player.rect.centerx = 640
            player.rect.bottom = 980
            pygame.sprite.groupcollide(mobs, player, True, True)



            for i in range(30):
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)
            # Обновление
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, False)
    for hit in hits:
        player.hp -= 1
        if player.hp <= 0:
            gameplay = False
    kek = pygame.sprite.collide_rect(player, boss)
    if kek:
        gameplay = False



    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()
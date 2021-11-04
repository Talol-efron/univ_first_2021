import pygame
import sys
import random
import math

img_bg = pygame.image.load("bgimage.png")
img_player = pygame.image.load("player1.png")
img_weapon = pygame.image.load("bullet.png")
img_enemy = [
    pygame.image.load("enemy1.png"),#敵画像
    pygame.image.load("e_bullet.png")#敵の攻撃弾画像
]
img_explode = [
    None,
    pygame.image.load("explode1.png"),
    pygame.image.load("explode2.png"),
    pygame.image.load("explode3.png"),
    pygame.image.load("explode4.png"),
    pygame.image.load("explode5.png"),
    pygame.image.load("explode6.png"),
    pygame.image.load("explode7.png")
]
img_gauge = pygame.image.load("gauge.png")#体力ゲージ
img_title = pygame.image.load("shoot_title.png")#タイトル画像
WHITE = (255,255,255)
BLACK = (0,0,0)
idx = 0#インデックス（ゲーム状態を管理する）
bg_y = 0
px = 320 #プレイヤーのX座標
py = 300 #プレイヤーのY座標
bx = 0 #弾のX座標
by = 0 #弾のY座標
t = 0 #タイマー変数
space = 0
score = 0
BULLET_MAX = 100 #弾の最大値
ENEMY_MAX = 100 #敵の最大数
ENEMY_BULLET = 1
bull_n = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX

ebull_n = 0
ebull_x = [0]*ENEMY_MAX
ebull_y = [0]*ENEMY_MAX
ebull_a = [0]*ENEMY_MAX
ebull_f =[False]*ENEMY_MAX
ebull_f2 = [False]*ENEMY_MAX
e_list = [0]*ENEMY_MAX
e_speed = [0]*ENEMY_MAX

EFFECT_MAX = 100 #エフェクトの最大数
e_n = 0
e_l = [0]*EFFECT_MAX
e_x = [0]*EFFECT_MAX #エフェクトのX座標
e_y = [0]*EFFECT_MAX #エフェクトのY座標

p_gauge = 100#HP
p_invincible = 0#無敵状態を管理する


def set_bullet():#弾のスタンバイ
    global bull_n
    bull_f[bull_n] = True
    bull_x[bull_n] = px-16
    bull_y[bull_n] = py-32
    bull_n = (bull_n+1)%BULLET_MAX

def move_bullet(screen):#弾を飛ばす
    for i in range(BULLET_MAX):
        if bull_f[i] == True:
            bull_y[i] = bull_y[i] - 32
            screen.blit(img_weapon,[bull_x[i],bull_y[i]])
            if bull_y[i] < 0:
                bull_f[i] = False

def move_player(screen,key):
    global px,py,space,p_gauge,p_invincible,idx,t
    if key[pygame.K_UP] == 1:
        py = py - 10
        if py < 20:
            py = 20
    if key[pygame.K_DOWN] == 1:
        py = py + 10
        if py > 460:
            py = 460
    if key[pygame.K_LEFT] == 1:
        px = px - 10
        if px < 20:
            px = 20
    if key[pygame.K_RIGHT] == 1:
        px = px + 10
        if px > 620:
            px = 620
    space = (space+1)*key[pygame.K_SPACE]
    if space%5 == 1: #5フレーム毎に弾を飛ばす
        set_bullet()
    if p_invincible%2 == 0:#無敵状態なら点滅させる
        screen.blit(img_player,[px-16,py-16])

    if p_invincible > 0:
        p_invincible = p_invincible - 1#無敵時は当たり判定を無効にする
        return
    elif idx == 1:
      for i in range(ENEMY_MAX):#敵との当たり判定をチェックする
        if ebull_f[i] == True:
            w = img_enemy[e_list[i]].get_width()
            h = img_enemy[e_list[i]].get_height()
            r = int((w+h)/4+(32+32)/4)
            if distance(ebull_x[i],ebull_y[i],px,py) < r*r:#敵及び敵の攻撃に接触
                effect(px,py)
                p_gauge = p_gauge - 20#ダメージを受ける
                if p_gauge <= 0:
                    idx = 2
                    t = 0
                if p_invincible == 0:
                    p_invincible = 30#無敵時間
                ebull_f[i] = False
                ebull_f2[i] = False

def set_enemy(x,y,a,enemy,speed):
    global ebull_n
    while True:
        if ebull_f[ebull_n] == False:
            ebull_f[ebull_n] = True
            ebull_x[ebull_n] = x
            ebull_y[ebull_n] = y
            ebull_a[ebull_n] = a
            e_list[ebull_n] = enemy
            e_speed[ebull_n] = speed
            break
        ebull_n = (ebull_n+1)%ENEMY_MAX

def move_enemy(screen):
    global score,idx,t
    for i in range(ENEMY_MAX):
        if ebull_f[i] == True:
            png = e_list[i]
            ebull_x[i] = ebull_x[i] + e_speed[i]*math.cos(math.radians(ebull_a[i]))
            ebull_y[i] = ebull_y[i] + e_speed[i]*math.sin(math.radians(ebull_a[i]))
            if e_list[i] == 0 and ebull_y[i] > 100 and ebull_f2[i] == False:#弾を発射
                set_enemy(ebull_x[i],ebull_y[i],90,1,15)
                ebull_f2[i] = True
            if ebull_x[i] < -40 or ebull_x[i] > 680 or ebull_y[i] < -40 or ebull_y[i] > 520:#画面外に敵が消える
                ebull_f[i] = False
                ebull_f2[i] = False

            if e_list[i] != ENEMY_BULLET:#敵の弾以外なら
                w = img_enemy[e_list[i]].get_width()
                h = img_enemy[e_list[i]].get_height()
                r = int((w+h)/4)+8
                for n in range(BULLET_MAX):
                    if bull_f[n] == True and distance(ebull_x[i]-16,ebull_y[i]-16,bull_x[n],bull_y[n]) < r*r:
                        bull_f[n] = False
                        effect(ebull_x[i],ebull_y[i])#エフェクト発生
                        score = score + 10#スコア加算
                        if score >= 100:
                            idx = 3
                            t = 0
                        ebull_f[i] = False
                        ebull_f2[i] = False
            rz = pygame.transform.rotozoom(img_enemy[png],-180,1.0)
            screen.blit(rz,[ebull_x[i]-rz.get_width()/2,ebull_y[i]-rz.get_height()/2])

def effect(x,y):#エフェクトを描画する準備を行う関数
    global e_n
    e_l[e_n] = 1
    e_x[e_n] = x
    e_y[e_n] = y
    e_no = (e_n+1)%EFFECT_MAX

def draw_effect(screen):#エフェクトを描画する関数
    for i in range(EFFECT_MAX):
        if e_l[i] > 0:
            rz = pygame.transform.rotozoom(img_explode[e_l[i]],0,0.5)#画像を縮小させる
            screen.blit(rz,[e_x[i]-30,e_y[i]-30])
            e_l[i] = e_l[i] + 1
            if e_l[i] == 8:#使用するエフェクト用画像が7枚
                e_l[i] = 0

def distance(x1,y1,x2,y2):
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def draw_text(screen,x,y,text,size,col):#文字表示の関数
    font = pygame.font.Font(None,size)
    s = font.render(text,True,col)
    x = x - s.get_width()/2
    y = y - s.get_height()/2
    screen.blit(s,[x,y])

def main():
    global t,bg_y,idx,score,p_gauge,p_invincible,px,py
    pygame.init()
    pygame.display.set_caption("シューティングゲーム")
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()

    while True:
        t=t+1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg_y = (bg_y+16)%480
        screen.blit(img_bg,[0,bg_y-480])
        screen.blit(img_bg,[0,bg_y])
        key = pygame.key.get_pressed()

        if idx == 0:#タイトル画面（仮）
            img_t = pygame.transform.rotozoom(img_title,0,0.8)
            screen.blit(img_t,[40,200])
            draw_text(screen,320,340,"PRESS SPACE!",80,WHITE)
            if key[pygame.K_SPACE] == 1:
                idx = 1
                t = 0
                score = 0
                px = 320
                py = 300
                p_gauge = 100
                p_invincible = 0
                for i in range(BULLET_MAX):
                    bull_f[i] = False
                for i in range(ENEMY_MAX):
                    ebull_f[i] = False

        if idx == 1:#ゲームプレイ中
            move_player(screen,key)
            move_bullet(screen)
            if t%30 == 0:#30フレームにつき敵1体出現
               set_enemy(random.randint(20,620),-10,90,0,6)
            move_enemy(screen)
        if idx == 2:#ゲームオーバー
            draw_text(screen,320,240,"GAMEOVER",100,WHITE)
            if t == 100:
                idx = 0
                t = 0
        if idx == 3:#ゲームクリア
            draw_text(screen,320,240,"GAMECLEAR",100,WHITE)
            if t == 100:
                idx = 0
                t = 0
        draw_effect(screen)
        if idx == 1:#ゲームプレイ中のみ体力ゲージとスコアを表示する
            screen.blit(img_gauge,(10,450))#体力ゲージ
            pygame.draw.rect(screen,(32,32,32),[10+p_gauge*2,450,(100-p_gauge)*2,25])#ダメージを受けたら矩形で塗りつぶす
            draw_text(screen, 580, 20, "SCORE" + str(score), 30, WHITE)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
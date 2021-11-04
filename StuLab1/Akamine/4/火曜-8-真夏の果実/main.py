import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply

from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("シューティングゲーム -- 真夏の果実")

background = pygame.image.load("images/background.png").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# BGMを導入する
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    pygame.mixer.music.play(-1)

    # myplaneを生成する
    me = myplane.MyPlane(bg_size)
    
    enemies = pygame.sprite.Group()

    # enemy planeを生成する
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)

    # 敵の中型航空機をスポーンします
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)

    # 敵の大型航空機をスポーンします
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)

    # 通常の弾丸を生成する
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # 超弾丸を生成する
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    for i in range(BULLET2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))

    clock = pygame.time.Clock()

    # ショットインデックス
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 統計スコア
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)

    # ゲームを一時停止するかどうかにフラグを立てる
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load(
        "images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load(
        "images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load(
        "images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    # 難易度を設定する
    level = 1

    # フルスクリーン爆弾
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 0

    # 30秒ごとにアイテムを配布します
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    # スーパーブレットタイマー
    DOUBLE_BULLET_TIME = USEREVENT + 1

    # ロゴが超弾丸を使用しているかどうか
    is_double_bullet = False

    # 無敵タイマーを無効にする
    INVINCIBLE_TIME = USEREVENT + 2

    # 命の数
    """
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 1
    """
    # ログファイルが繰り返し開かれるのを防ぐために使用されます
    recorded = False

    # ゲームオーバー画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 写真を切り替えるために使用されます
    switch_image = True

    # 遅延の場合
    delay = 100

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                       paused_image = pause_nor_image

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)

            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        # ユーザーのスコアに基づいて難易度を上げる
        if level == 1 and score > 5000:
            level = 2
            upgrade_sound.play()
            # 小型敵機3機、中型敵機2機、大型敵機1機を追加
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            # 小さな敵機の速度を上げる
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 30000:
            level = 3

            me.hp = 100

            upgrade_sound.play()
            # 小型敵機5機、中型敵機3機、大型敵機2機を追加
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 小さな敵機の速度を上げる
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 60000:
            level = 4
            upgrade_sound.play()
            # 小型敵機5機、中型敵機3機、大型敵機2機を追加
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 小さな敵機の速度を上げる
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 100000:
            level = 5

            me.hp = 150

            upgrade_sound.play()
            # 小型敵機5機、中型敵機3機、大型敵機2機を追加
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 小さな敵機の速度を上げる
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)

        screen.blit(background, (0, 0))

        if me.hp and not paused:
            # ユーザーのキーボード操作を検出する
            key_pressed = pygame.key.get_pressed()

            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 全画面爆弾の供給を描画し、それが取得されているかどうかを確認します
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # 超弾丸の補給品を引き、入手できるか確認する
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
                    bullet_supply.active = False

            # 弾丸を発射する
            if not(delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset(
                        (me.rect.centerx-33, me.rect.centery))
                    bullets[bullet2_index +
                            1].reset((me.rect.centerx+30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

            # 弾丸が敵の航空機に当たるかどうかを検出します
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(
                        b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            # 大きな敵機を描く
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    # ヘルスバーを描く
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     2)
                    # 20％を超える寿命は緑で表示され、それ以外の場合は赤で表示されます。
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)

                    # 画面に表示され、効果音を再生します
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    # 破壊
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(
                            each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 10000
                            each.reset()

            # 中型の敵機を引く：
            for each in mid_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # ヘルスバーを描く
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     2)
                    # 体力が20％を超えると緑色になり、それ以外の場合は赤色になります。
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)
                else:
                    # 破壊
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(
                            each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 6000
                            each.reset()

            # 小さな敵の飛行機を描きます：
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 破壊
                    if not(delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(
                            each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            # 自機の当たり判定
            #引数,meとenemiesの接触があるかの判定をする --> pygame.sprite.spritecollide()
            enemies_down = pygame.sprite.spritecollide(
                me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 飛行機を描く
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 破壊
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        #モブ、中ボス、大ボスごとにif文でhpの減少幅を変えたい###############################
                        small_enemies_down = pygame.sprite.spritecollide(
                            me, small_enemies, False, pygame.sprite.collide_mask)
                        mid_enemies_down = pygame.sprite.spritecollide(
                            me, mid_enemies, False, pygame.sprite.collide_mask)
                        big_enemies_down = pygame.sprite.spritecollide(me, big_enemies, False, pygame.sprite.collide_mask)
                        if big_enemies_down:
                            me.hp = 0
                        elif mid_enemies_down:
                            if me.hp >= 50:
                                me.hp -= 50
                            else:
                                me.hp = 0
                        else:
                            me.hp -=25
                        #me.hp -= 50
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            # フルスクリーン爆弾の数を描画します
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width,
                                    height - 5 - text_rect.height))
            """
            # 残りの命の数を表示する
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,
                                (width-10-(i+1)*life_rect.width,
                                 height-10-life_rect.height))
            """
            #HP表示#################################################################
            # ヘルスバーを描く
            pygame.draw.line(screen, BLACK,
                                (me.rect.left, me.rect.top + 130),
                                (me.rect.right, me.rect.top + 130),10)
            # 20％を超える寿命は緑で表示され、それ以外の場合は赤で表示されます。
            energy_remain = me.hp / 150
            if energy_remain > 0.2:
                energy_color = GREEN
            else:
                energy_color = RED
            """
            pygame.draw.line(screen, energy_color,
                                (me.rect.left, me.rect.top - 5),
                                (me.rect.left + me.rect.width * energy_remain,
                                me.rect.top - 5), 2)
            """    
            pygame.draw.line(screen, energy_color,
                                (me.rect.left, me.rect.top + 130),
                                (me.rect.left + me.rect.width * energy_remain,
                                me.rect.top + 130), 5)
            
            "screen.blit(bomb_text, (20 + bomb_rect.width,height - 5 - text_rect.height))"

            # スコアを表示
            score_text = score_font.render(
                "Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))

        # ゲーム終了画面を描く
        elif me.hp == 0:
            # BGMが停止しました
            pygame.mixer.music.stop()

            # すべての音楽を停止します
            pygame.mixer.stop()

            # サポートの発行を停止する
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not recorded:
                recorded = True
                # 歴史上最高のスコアを読む
                with open("record.txt", "r") as f:
                    record_score = int(f.read())

                # プレーヤーのスコアが過去の最高スコアよりも高い場合は、保存します
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))

            # 終了画面を描画します
            #rectは座標を示す
            """
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            record_score_text_rect = record_score.get_rect()
            record_score_text_rect.left, record_score_text_rect.top = \
                (width - record_score_text_rect.width) // 2, height // 3
            screen.blit(record_score_text, record_score_text_rect)
            """
            #"YOUR SCORE : xxx" の表示
            gameover_text1 = gameover_font.render("Your Score : %d" % score, True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

         
            #歴代レコードの表示
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            record_score_text_rect = record_score_text.get_rect()
            record_score_text_rect.left, record_score_text_rect.top = \
                (width - record_score_text_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(record_score_text, record_score_text_rect)
       
            
            """
            #SCOREの表示
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)
            """
            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                record_score_text_rect.bottom + 50
            screen.blit(again_image, again_rect)
    

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # ユーザーのマウス操作を検出する
            # ユーザーがマウスの左ボタンを押した場合
            if pygame.mouse.get_pressed()[0]:
                # マウスの座標を取得する
                pos = pygame.mouse.get_pos()
                # ユーザーが「再起動」をクリックした場合
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    # main関数を呼び出して、ゲームを再開します
                    main()
                # ユーザーが「ゲーム終了」をクリックした場合
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # ゲームを終了します
                    pygame.quit()
                    sys.exit()

        # 一時停止ボタンを描画
        screen.blit(paused_image, paused_rect)

        # 画像を切り替える
        if not(delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()


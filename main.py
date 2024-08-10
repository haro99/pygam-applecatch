# import pygame   # Pygameをインポート

# pygame.init()   # Pygameを初期化
# screen = pygame.display.set_mode((800, 600))    # 画面作成
# image = pygame.image.load("icon.png")   # 画像読み込み
# running = True  # 実行継続フラグ
# (x, y) = (32,32)

# while running:
#     for event in pygame.event.get():    # イベントのリストを得る
#         if event.type == pygame.QUIT:   # 種類がQUITなら
#             running = False   # 終了

#     screen.fill((0, 0, 0))  # 画面を塗りつぶす
#     screen.blit(image, (x, y))  # 描画
#     pygame.display.flip()   # 画面フリップ

#     # Playerの位置を少しずつ移動させる
#     x += 1
#     y += 1
#     pygame.time.wait(10) # 更新間隔。多分ミリ秒

# pygame.quit()   # Pygameを終了

import pygame
from pygame.locals import *
import sys
import random

apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (70, 70))
basket = pygame.image.load("basket.png")
basket = pygame.transform.scale(basket, (66, 41))

class position:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    appleslist = []

    #UFOの初期設定
    ux = 200
    uy = 100
    # サイズ
    uw = 50
    uh = 50
    uvx = 0.05
    uhp = 100

    # プレイヤの初期設定
    px=120
    py=500

    # スコア
    score = 0

    font = pygame.font.SysFont(None, 50)


    # タマの初期設定
    # tx=px+25
    # ty=py
    # tvy = 0
    for i in range(5):
        appleslist.append(position(random.randrange(70) * 10,  -random.randrange(100)))

    while True:

        #画面を消去
        screen.fill((255,255,255))                                    # 背景を白

        #UFOの移動の処理と描画
        # ux = ux + uvx
        for i in range(len(appleslist)):
             appleslist[i].y += uvx
        # 重力処理
        # uy += uvx

        for i in range(len(appleslist)):
            # ある程度落下したら
            if  appleslist[i].y > 600:
                # y座標を0にしてX座標をランダムな位置に設定
                appleslist[i].y = 0 - random.randrange(10) * 10
                appleslist[i].x = random.randrange(70) * 10
                #  print(ux)
                #  appleslist.append(position(random.randrange(70), 0))
        
        for pos in appleslist:
            screen.blit(apple, (pos.x, pos.y))

        # if ux > 700 or ux < 0:
        #     uvx *= -1
        for i in range(len(appleslist)):
            # 当たり判定    
            if (px <= appleslist[i].x <= px + uw) and (py <= appleslist[i].y <= py + uh):
                appleslist[i].y = 0 - random.randrange(10) * 10
                appleslist[i].x = random.randrange(70) * 10
                score += 10

        text = font.render(str(score), True, (0, 0, 0))
        # if uhp > 0:    
            # pygame.draw.rect(screen, (0,255,0), Rect(ux,uy,uw,uh), 1)    # ■
        # screen.blit(apple, (ux, uy))

        # #タマの処理と描画
        # ty = ty + tvy
        # pygame.draw.circle(screen,(10,10,10),(tx,ty),5)              # ●

        #プレイヤの処理と描画
        screen.blit(basket, (px, py))    # ■
        # pygame.draw.line(screen, (0,255,0), (0,200), (100,300), 2)    # 線

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら
                pygame.quit()             # 全てのpygameモジュールの初期化を解除
                sys.exit()                # 終了（ないとエラーで終了することになる）
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                px -= 0.1  # 横方向、変数名pvxはpxにします。
                # tx = px+25
        if keys[pygame.K_RIGHT]:
                px += 0.1  # 横方向、変数名pvxはpxにします。
                # tx = px+25


        screen.blit(text,(40, 30))
        pygame.display.update()                                       # 画面更新

if __name__ == "__main__":
    main()

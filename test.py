# -*- coding: utf-8 -*-

import os
import pygame

# GUIなし環境でのエラー回避設定
os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

# 画面サイズを設定（実際にはウィンドウは表示されない）
W, H = 500, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pygame Drawing Test")

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 画面の背景を塗りつぶし、円を描画
screen.fill(WHITE)
pygame.draw.circle(screen, BLUE, (W//2, H//2), 50)

# 画面を更新（GUIなし環境では実際には何も表示されない）
pygame.display.flip()

# 2秒待機してから終了
pygame.time.wait(2000)

pygame.quit()
print("Pygame処理が完了しました！")

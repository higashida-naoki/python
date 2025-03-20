import pygame

#画面サイズを定義
W, H = 320, 270

#タイル数
TILE_X = 16
TILE_Y = 14


def main():
    ''' メイン関数
    '''
    #pygame初期化
    pygame.init()
    #画面を作成
    win = pygame.display.set_mode((W, H))
    #クロックを生成
    clock = pygame.time.Clock() #１秒間に何コマ動くか

    #イベントループ
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                #マウスの左ボタンが押された時の処理
                hoge = 3
                

if __name__ == '__main__':
    main()
#! python3
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 上午12:48
# @Author  : BlingBling
# @Site    : 
# @File    : 510KGame.py
# @Software: PyCharm Community Edition

import pygame
import sys, random, copy
from pygame.locals import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CARD_HEIGHT = 64
CARD_WIDTH = 48
FPS = 30
BACKGROUND_COLOR = 60,179,113
WHITE = 255,255,255

def main():
    global FPSCLOCK, DISPLAYSURF, CARD_BACK_IMAGE
    # 初始化pygame各个模块
    pygame.init()

    # 创建游戏窗口
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # 游戏窗口标题
    pygame.display.set_caption(u"510K Games")

    # 载入扑克牌背面图片,并缩放大小
    CARD_BACK_IMAGE = pygame.image.load("card_back.png")
    CARD_BACK_IMAGE = pygame.transform.smoothscale(CARD_BACK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

    isFirstGame = True

    while True:
        runGame(isFirstGame)
        isFirstGame = False


def runGame(isFirstGame):
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()

        DISPLAYSURF.fill(BACKGROUND_COLOR)
        DISPLAYSURF.blit(CARD_BACK_IMAGE, (100,100))
        font = pygame.font.Font(None, 60)
        textImage = font.render("hello", True, WHITE)
        DISPLAYSURF.blit(textImage, (100, 100))
        pygame.display.update()

if __name__ == '__main__':
    main()
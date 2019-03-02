import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''创建表示敌人的类'''

    def __init__(self,ai_settings,screen):
        '''对敌人进行初始化并设置其位置'''
        super(Alien,self).__init__()
        self.screen = screen#将游戏窗口加入到这里
        self.ai_settings = ai_settings#将参数进行赋值

        #加载敌人图像，并设置rect属性
        self.image = pygame.image.load('imges/boss.bmp')
        self.rect = self.image.get_rect() #运用get_rect()方法得到敌人飞机的rect

        #每个敌人飞机的初始位置都是在左上角附近
        '''将飞机的rectwidth和height赋值给飞机的x,y'''
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储敌人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):#对敌人飞机的位置进行修改
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction 
        self.rect.x = self.x; #将新的位置的矩阵的x赋值

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

        

        

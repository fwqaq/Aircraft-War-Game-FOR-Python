#对子弹进行类的创建
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):  #将Bullet类继承Sprite，Sprite精灵类
    def __init__(self,ai_settings,screen,ship):
        '''在飞船所处的位置创建子弹'''
        super(Bullet,self).__init__()  #对Sprite中的__init__（）进行重写
        self.screen = screen

        #在0,0的位置创建一个子弹的矩阵
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  #将飞船的centerx赋值给子弹的centerx,centerx是二维坐标的横坐标
        self.rect.top = ship.rect.top #将飞船的top属性和子弹的top属性进行赋值，
        '''矩阵rect的属性有top bottom right size width height center'''
        #其中center为矩形的中心店，关于横纵坐标的二元组，所以有centerx，和centery,还有x,y属性

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor #将Setting()类中的属性传递给bullet类

    def update(self):
        '''子弹向上移动'''
        self.y  -= self.speed_factor #子弹向上移动后的位置
        self.rect.y = self.y  #将移动后的位置赋值给矩阵的y值

    def draw_bullet(self):
        '''在屏幕中绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        

        
    

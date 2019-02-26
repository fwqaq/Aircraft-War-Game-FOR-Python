import pygame
from settings import Setting  #导入初始化的包
from pygame.sprite import Group  #导入sprite中的Group的包
from ship import Ship  #导入飞船的包
import game_funtion as gf
from alien import Alien #导入敌人飞船的包
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
def run_game():

    #对Setting进行实例化
    ai_settings = Setting() #对所有设置的类中进行实例化
    
    #初始化游戏并且创建一个屏幕
    pygame.init()  #初始化背景设置，让python能够正常工作
    
    #设置背景颜色，将背景颜色设置为230,230,230
    bg_color = (ai_settings.bg_color)
    
    #创建一个screen的显示窗口（1200,800）是一个元组，设置屏幕的大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    pygame.display.set_caption('Alien Invasion')#对游戏的名字进行设
    background = pygame.image.load('imges/bg.bmp')
    
    #加入一个飞机类........'''对飞船的初始化中有了关于对飞船速度的设置'''
    ship = Ship(ai_settings,screen) 
    #创建一个Group()的实例，用来储存子弹类
    bullets = Group()
    #加入一个敌人飞机的类的Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个按钮
    play_button = Button(ai_settings,screen,'play')
    #创建一个游戏信息类
    stats = GameStats(ai_settings)
    #创建一个游戏分数的类
    sb = Scoreboard(ai_settings,screen,stats)
    #开始游戏的主循环
    while True:
        #添加监视键盘和鼠标事件,在函数类的check_event()函数中
        gf.check_event(stats,play_button,aliens,bullets,ai_settings,screen,ship) 
        if stats.game_active:
            ship.update()   #对飞船的位置进行修改
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            gf.update_bullet(bullets,aliens,ai_settings,sb,stats)#对子弹进行移动和消失的子弹在Group中进行移除
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb) #对飞机和子弹、敌人飞机的新位置不断进行更新
run_game()

import sys
import pygame
from bullet import Bullet
from alien import Alien
import random

def check_event(stats,play_button,aliens,bullets,ai_settings,screen,ship):#将键盘和鼠标事件的监视写为check_event()函数
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #检测按下的键
                elif event.type == pygame.KEYDOWN:
                    check_keydown(event,ship,ai_settings,screen,bullets) #检测空格键并且进行添加新的bullet
                    check_keydown(event,ship,ai_settings,screen,bullets)
                 #检测松开的键       
                elif event.type == pygame.KEYUP: 
                    check_keyup(event,ship)
                elif event.type == pygame.MOUSEBUTTONDOWN:#检测鼠标点击事件
                    mouse_x,mouse_y = pygame.mouse.get_pos()  #得到鼠标点击的位置，返回一个数组
                    check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settings,screen,ship)
def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settings,screen,ship): #检测鼠标点击到的位置是不是按钮的位置
    #用collidepoint()检测鼠标点击的矩阵是不是和play的rect内部
    button_click = play_button.rect.collidepoint(mouse_x,mouse_y)
    if play_button.rect.collidepoint(mouse_x,mouse_y) and button_click:
        stats.reset_stats() #重置游戏的统计信息
        stats.game_active = True
        #清空子弹飞船
        aliens.empty()
        bullets.empty()
        #重新创建新的飞机
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        pygame.mouse.set_visible(False) #在打开鼠标后将鼠标的光标进行隐藏，一面在游戏的时候点到了play按钮
        
def check_keydown(event,ship,ai_settings,screen,bullets):#对于按键是否按下的检测
    if event.key == pygame.K_RIGHT:  #检测按下的是不是右键 
        #飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: #检测按下的是不是左键
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:#检测按下的是不是空格键
        if len(bullets)<ai_settings.bullet_number:
            new_bullet = Bullet(ai_settings,screen,ship) #如果是空格键就创建一个新的子弹类
            bullets.add(new_bullet)#将子弹类加入到bullets的Group类中

def check_keyup(event,ship):#对于键盘松开的检测
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb): #屏幕刷新所有的飞机和子弹都需要进行更新位置
    #在每次循环中都进行对屏幕的更新，使用fill()函数将bg_color填充在整个屏幕中
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() #在制定的位置设置一个新的飞机，在屏幕更新后就相当于飞机进行了移动s
    aliens.draw(screen)
   #让屏幕的将不断更新，以显示元素的新位置
    sb.show_score()
    if  not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    

def  update_bullet(bullets,aliens,ai_settings,sb,stats):
        bullets.update() #对子弹的向上移动进行修改
        #在game_funtion()中调用屏幕刷新的函数
        for bullet in bullets.copy():  #对子弹的列表创建一个副本，并且遍历
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)  #如果越界就从bullets中移除
        '''重点 高效'''
        #用pygame中的sprite.groupcollide()  来判断两个Group是否有碰撞。。。
        collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
        if collisions:
            stats.score += ai_settings.alien_points
            sb.prep_score()

#对敌人飞船位置的修改
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,screen,ship,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(screen,aliens)
    
def check_aliens_bottom(screen,aliens):#检测敌人飞船是不是接触到了屏幕底部，如果是将从aliens中移除
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            aliens.remove(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建一个外星人组'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width  #外星人矩阵的宽度存储到alien_width中
    number_aliens_x = get_number_aliens_x(ai_settings,alien_width)#得到一排飞机的数量
    #number_rows = get_number_row(ai_settings,ship.rect.height,alien.rect.height) #得到共有几排可以加载飞机
    #创建一行机器人
    #for row_number in range(number_rows):
    aliens_numbers = random.randint(2,number_aliens_x-2)
    position = []
    boolean = True
    while boolean:
        a = random.randint(1,number_aliens_x-1)
        if a not in position:
            position.append(a)
        if len(position) == aliens_numbers:
            boolean = False
    position.sort()
    print(position)
    for alien_number in position: #设置参数alien_number和range（）
        create_alien(ai_settings,screen,aliens,alien_number) #row_number
    del(position)

def create_alien(ai_settings,screen,aliens,alien_number):#,row_number
    alien = Alien(ai_settings,screen)#添加一个敌人飞机
    alien_width = alien.rect.width
    alien.x =alien_width + 2*alien_width*alien_number#敌人的横坐标是不断的增加的，加上了中间的空留
    alien.rect.x = alien.x   #将横坐标赋值给飞机矩阵的横坐标
    alien.rect.y = 0
    aliens.add(alien)  #添加到aliens中去

#得到一排的飞机数量
def get_number_aliens_x(ai_settings,alien_width):  #得到一排的敌人飞机数量
    available_space_x = ai_settings.screen_width-2*alien_width#屏幕宽度-外星人飞船的的2倍，在两边是没有机器人的
    number_aliens_x = int(available_space_x /(2*alien_width))   #一排的敌人飞船的个数
    return number_aliens_x

#得到整个屏幕可以有多少行飞机
def get_number_row(ai_settings,ship_height,alien_height):#得到行数的函数
    #行数= 屏幕的高度-3*敌人飞机的高度-大飞船的高度。3倍是因为留出一行给飞船进行击杀敌人
    available_space_y = (ai_settings.screen_height - (3*alien_height)-ship_height)#计算可以装飞船的高度
    number_rows = int(available_space_y /(2*alien_height))
    return number_rows #返回计算出来能够进行敌人飞船的行数

def check_fleet_edges(ai_settings,screen,ship,aliens):
    '''检测敌人飞船到达左右两边的时候的操作'''
    for alien in aliens.sprites(): #对aliens中进行检测
        if alien.check_edges(): #调用是否越界的函数，越界返回True否则返回False
            change_fleet_edges(ai_settings,screen,ship,aliens)#改变越界进行处理函数   
            break

def change_fleet_edges(ai_settings,screen,ship,aliens):
    '''越界处理函数越界则往下移动settings中参数的像素'''
    for alien in aliens.sprites():
        alien.rect.y +=  alien.rect.height
    ai_settings.fleet_direction *= -1  #一方改变则让飞船向另一个方向移动
    create_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应飞船被撞击到'''
    if stats.ships_left >0 :
        stats.ships_left -= 1

        #清空子弹和敌人飞机
        aliens.empty()
        bullets.empty()
        stats.score = 0
        
        #重新创建新的敌人飞机
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)#当游戏结束的时候将鼠标的光标、显示出来








        
    
       
    

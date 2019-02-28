import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞飞船的并设置其初始位置"""
        self.screen = screen#screen是显示窗口，这是将飞船添加在screen的窗口中

        self.ai_settings = ai_settings #将所有的类的实例化加入在进来
        
        #加载飞机图像并获取外接矩阵
        self.image = pygame.image.load('imges/plane.bmp')  #调用此函数进行图片的加载

        #获取 Surface 对象的矩形区域
        self.rect = self.image.get_rect() #在加载图像后用get_rect()获取相应的surface的属性rect
        self.screen_rect = screen.get_rect()#对飞船的图像矩阵进行储蓄

        #将每个新的飞船进行位置的设置
        self.rect.centerx = self.screen_rect.centerx #将飞机中心的x的坐标设置为表示屏幕的矩阵的属性centerx
        self.rect.bottom = self.screen_rect.bottom#将下边缘坐标设置为便是屏幕的矩阵的属性bottom

        #在飞船的属性中center中存储小数值,并且这个数就等于self.rect.centerx，就是子啊矩阵的属性的值
        self.center = float(self.rect.centerx)#'''这是一个添加的属性center'''#加入一个属性center

        #加入两个位移标志，如果是True就移动，初始化为False
        self.moving_right =False
        self.moving_left = False
        

    def update(self):
        #对飞船和screen界面的矩阵右边界进行对比，从左到右是从0到最大值的数字
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        #对两个矩阵的左边距进行比较，screen的左边距是0，
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #将更新后的数据赋值给矩阵的属性recr.centerx
        self.rect.centerx = self.center
        
    def blitme(self):
        """在制定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
        
        

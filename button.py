import pygame.font

class Button():


    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的属性
        self.width,self.height = 200,50 #设置按钮的长度和宽度
        self.button_color=(0,250,0) #设置按钮的颜色
        self.text_color = (255,255,255) #设置文本的颜色
        self.font = pygame.font.SysFont(None,48) #设置使用什么字体来渲染文本  None是默认字体，48是字体的大小

        #创建按钮的rect对象，并且为之居中
        self.rect = pygame.Rect(0,0,self.width,self.height) #创建按钮的rect对象
        self.rect.center = self.screen_rect.center #是按钮对象在屏幕的中间

        #按钮标签设置一次
        self.prep_msg(msg)  #设置按钮的标签

    def prep_msg(self,msg):
        '''调用font.render()函数将文本转换为图片'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color) #调用font.render()函数
        self.msg_image_rect = self.msg_image.get_rect() #得到图片的rect对象
        self.msg_image_rect.center = self.rect.center#让文本显示在按钮的中间

    def draw_button(self):
        #绘制一个用颜色填充的颜色，在绘制按钮的颜色
        self.screen.fill(self.button_color,self.rect)   #用颜色填充在self.rect中，  fill()
        self.screen.blit(self.msg_image,self.msg_image_rect) #将按钮放置到screen中去。


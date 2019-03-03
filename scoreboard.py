import pygame.font
class Scoreboard():
    '''显示得分的类'''
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息的字体
        self.text_color = (30,30,30)
        #设置文本的字体大小和字体格式。调用pygame.font.SysFont()函数
        self.font = pygame.font.SysFont(None,48) 

        #显示图像函数设置
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        #调用font.render()函数让文本变为一个image型，
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #将得分放在右上角 ，设置score_rect在screen中的位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20 
    #显示分数图像函数
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect) #将分数页面显示在screen中去

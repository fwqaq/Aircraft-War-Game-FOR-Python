class  GameStats():
    '''跟踪游戏的数据'''
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        '''初始化在游戏中可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
    

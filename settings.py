class Setting():
    """存储《游戏》所有设置的类"""
    def __init__(self):
        #初始化游戏的设置，屏幕宽度和北疆颜色
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color= (230,230,230)

        #加入飞船的速度参数，对飞船进行参数的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3 #设置飞船的数量
        #加入子弹的参数并且对子弹的参数进行初始化
        self.bullet_speed_factor = 1  #子弹的速度
        self.bullet_width = 3#子弹的宽
        self.bullet_height = 15   #子弹的长度
        self.bullet_color = (60,60,60)   #子弹的颜色
        self.bullet_number = 10 #添加子弹的个数参数

        #设置敌人飞船的速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 0.1#设置下降的速度为10
        self.fleet_direction = 1 #此参数表示移动的方向 1 向右移动，  -1向左移动

        #设置游戏每个等级应该飞船增加的速度
        self.speedup_scale = 0.1
        self.alien_points = 1#每个飞机的分数

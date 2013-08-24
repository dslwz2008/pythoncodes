import cocos
from cocos.actions import *
from cocos.sprite import *
from euclid import Vector2, Vector3
from cocos.rect import Rect
from cocos.scenes.transitions import *
from cocos.director import director
from cocos.audio.effect import Effect
import mathtool
import pyglet
import math
import random

class MainScene(cocos.layer.Layer):
    
    is_event_handler = True
    
    def __init__(self):
        super( MainScene, self ).__init__()
        
        win_x, win_y = cocos.director.director.get_window_size()
        self.background = Sprite('bg.jpg')
        self.background.position = win_x / 2, win_y / 2
        self.add(self.background)
        
        self.shooter = Sprite('Player2.png')
        self.shooter.position = self.shooter.width / 2, win_y / 2
        self.add(self.shooter)
        
        self.monsters = []
        self.projectiles = []
        self.schedule_interval(self.update, 1.0)
        self.schedule(self.frame)
        #self.pos_text = cocos.text.Label('move your mouse', font_size=18, x=100, y=100)
        #self.add(self.pos_text, z=1)
        cocos.audio.pygame.mixer.music.load('POWERLESS.mp3')
        cocos.audio.pygame.mixer.music.play(-1, 0.0)
    
    def frame(self, dt):
        if not self.monsters or not self.projectiles: 
            pass
        proj_delete = []
        mons_delete = []
        for projectile in self.projectiles:
            for monster in self.monsters:
                rect_proj = projectile.get_rect()
                rect_mons = monster.get_rect()
                if rect_proj.intersects(rect_mons):
                    proj_delete.append(projectile)
                    mons_delete.append(monster)
                    self.monsters.remove(monster)
                    self.projectiles.remove(projectile)
                    self.remove(monster)
                    self.remove(projectile)
                    print 'pang!'
                    effect = Effect('powerup.wav')
                    effect.play()
        
        del proj_delete
        del mons_delete
    
    def update(self, second):
        #print 'aaa'
        self.monster = Sprite('Target.png')
        win_x, win_y = cocos.director.director.get_window_size()
        offset = self.monster.height/2
        pos_y = random.random() * (win_y - self.monster.height) + offset
        self.monster.position = win_x, pos_y
        target_pos = -self.monster.width / 2, pos_y
        self.monster.do(MoveTo(target_pos, 2) + CallFunc(self.move_finish, self.monster))
        self.add(self.monster)
        self.monsters.append(self.monster)
    
    def move_finish(self, target):
        if target in self.monsters:
            self.monsters.remove(target)
            print "del monster"
        gameover_layer = GameOverLayer()
        gameover_scene = cocos.scene.Scene (gameover_layer)
        cocos.director.director.replace( FadeTRTransition(gameover_scene, duration=2) )
        cocos.audio.pygame.mixer.music.stop()
    
    def update_text(self, x, y):
        text = '%d,%d' % (x, y)
        self.pos_text.element.text = text
        self.pos_text.element.x = x
        self.pos_text.element.y = y
        
    def rotate_shooter(self, x, y, dx, dy):
        ox, oy = self.shooter.position
        vec_last = Vector3(x+dx-ox, y+dy-oy, 0)
        vec_new = Vector3(x - ox, y - oy, 0)
        dir = vec_last.cross(vec_new)
        angle = mathtool.get_angle_of_2vectors(vec_last,  vec_new)
        print angle
        if dir.z > 0:
            self.shooter.do(RotateBy(angle, 0.1))
        else:
            self.shooter.do(RotateBy(-angle, 0.1))
        
        
    def on_mouse_motion(self, x, y, dx, dy):
        #dx,dy they give the distance the mouse travelled along each axis to get to its present position
        #self.update_text(x, y)
        #self.rotate_shooter(x, y, dx, dy)
        pass
        
    def on_mouse_press (self, x, y, buttons, modifiers):
        ox, oy = self.shooter.position
        theta = mathtool.radian2angle(math.atan2(y - oy, x - ox))
        #print ox, oy, x, y, theta
        act_rotate_finish = CallFunc(self.rotate_finish,  x, y)
        self.shooter.do(RotateTo(-theta, 0.2) + act_rotate_finish)
        
    def rotate_finish(self, x, y):
        self.nextprojectile = Sprite('Projectile2.png')
        ox, oy = self.shooter.position
        self.nextprojectile.position = ox, oy
        self.add(self.nextprojectile)
        win_x, win_y = cocos.director.director.get_window_size()
        offsetx = win_x - ox
        offsety = offsetx * (y - oy) / float(x - ox)
        dest = offsetx + ox*2, offsety + oy
        #print x, y, offsetX, offsetY, dest
        act_shoot_finish = CallFunc(self.shoot_finish, self.nextprojectile)
        self.nextprojectile.do(MoveTo(dest, 1) + act_shoot_finish)
        self.projectiles.append(self.nextprojectile)
        
    def shoot_finish(self, target):
        if target in self.projectiles:
            self.projectiles.remove(target)
            print "del projectile"
            
class GameOverLayer(cocos.layer.ColorLayer):
    def __init__(self):
        super(GameOverLayer, self).__init__(255, 255, 255, 128)
        
        win_x, win_y = cocos.director.director.get_window_size()
        self.text = cocos.text.Label('Game Over!', anchor_x='center', anchor_y='center')
        self.text.position = win_x / 2, win_y / 2
        self.add(self.text)

if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    director.init(width=480,  height=320, audio_backend='sdl')

    # We create a new layer, an instance of HelloWorld
    mainscene_layer = MainScene ()

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (mainscene_layer)

    # And now, start the application, starting with main_scene
    director.run (main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )

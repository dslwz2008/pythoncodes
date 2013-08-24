import cocos
from cocos.actions import *

class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super( HelloWorld, self ).__init__(64,64,224,255)

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a cocosnode
        label = cocos.text.Label('Hello, World!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 320,240
        self.add( label )
        
        witch = cocos.sprite.Sprite('witch-standing.png')
        witch.position = 240, 320
        self.add(witch)
        
        scale = ScaleBy(3, duration = 2)
        witch.do(Repeat(Reverse(scale) + scale))
        
        rot = RotateBy(360, 2)
        witch.do(Accelerate(rot) + Accelerate(Reverse(rot)))
        
        

if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld ()

    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run (main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )
